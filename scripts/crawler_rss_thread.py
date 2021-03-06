__author__ = 'nolram'

import sys
import django
import requests
import feedparser as fp

from Crawler.models import LinksRSS, Postagens, TagsPostagens, Tags
from Crawler.rssmodel import RSSModel

from requests.exceptions import ConnectionError, TooManyRedirects

from django.db.utils import IntegrityError
from django.db import close_old_connections
from django.db.models import F

from threading import Thread
from queue import Queue
from datetime import datetime

CONCURRENT = 25

DEBUG = True

django.setup()

def do_crawling(q):
    """
    Função de crawling de notícias pelos links RSS.
    IMPORTANTE: Se houver alguma excessão não tratada a função nunca chegará em q.task_done()
    e a Thread nunca se encerrará
    :param q: Queue()
    :return: None
    """
    while True:
        site = q.get()
        if DEBUG:
            mensagem = ""
            mensagem += "== {0} - Coletando: {1} == \n".format(datetime.now(), site.link_rss)
        coleta = fp.parse(site.link_rss)
        if "entries" in coleta:
            for col in range(0, len(coleta.entries)):
                if col <= 50:
                    try:
                        post = Postagens.objects.get(link_origi=coleta.entries[col].link)
                    except Postagens.DoesNotExist:
                        try:
                            s = requests.get(coleta.entries[col].link)
                        except ConnectionError:
                            mensagem += "ERRO: ConnectionError: {0}".format(coleta.entries[col].link)
                            break
                        except TooManyRedirects:
                            mensagem += "ERRO: TooManyRedirects: {0}".format(coleta.entries[col].link)
                            break
                        if s.status_code == 200 or s.status_code == 301:
                            try:
                                rss_model = RSSModel(coleta.entries[col], s.url, coleta.entries[col].link, site)
                                post = Postagens(titulo=rss_model.titulo,
                                                 link=rss_model.link,
                                                 link_origi=rss_model.link_real,
                                                 texto=rss_model.texto,
                                                 fk_rss=rss_model.fk_rss,
                                                 fk_imagem=rss_model.imagem_banco)
                                post.save()

                                tags = []
                                for t in rss_model.tags:
                                    try:
                                        db_tag = Tags.objects.get(tag=t)
                                        db_tag.contador = F('contador') + 1
                                        db_tag.save()
                                        tags.append(db_tag)
                                    except Tags.DoesNotExist:
                                        db_tag = Tags(tag=t)
                                        db_tag.save()
                                        tags.append(db_tag)

                                for tag in tags:
                                    try:
                                        TagsPostagens.objects.get(fk_tag=tag, fk_postagem=post)
                                    except TagsPostagens.DoesNotExist:
                                        tpos = TagsPostagens(fk_tag=tag, fk_postagem=post)
                                        tpos.save()
                            except IntegrityError:
                                mensagem += "ERRO: Valor já inserido no banco: {0}".format(s.url)
                        else:
                            mensagem += "ERRO: código retornado pelo site: {0}".format(s.status_code)

                    except Postagens.MultipleObjectsReturned:
                        if DEBUG:
                            mensagem += "ERRO: Multiplos objetos Retornados - {0} \n".format(
                                coleta.entries[col].link)
                        else:
                            pass
        else:
            if DEBUG:
                mensagem += "A consulta não retornou resultados \n"
            else:
                pass
        if DEBUG:
            mensagem += "==== {0} - Coleta Concluida - {1} ==== \n".format(datetime.now(), site.link_rss)
            print(mensagem)
        close_old_connections()
        q.task_done()

def testar():
    sites = LinksRSS.objects.all()
    q = Queue()
    for i in range(CONCURRENT):
        t = Thread(target=do_crawling, args=(q,))
        t.setDaemon(True)
        t.start()

    try:
        for site in sites:
            q.put(site)
        q.join()
    except KeyboardInterrupt:
        sys.exit(1)
