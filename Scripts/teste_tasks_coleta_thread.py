__author__ = 'nolram'

import sys
import requests
import feedparser as fp

from Crawler.models import LinksRSS, Postagens, TagsPostagens, Tags
from Crawler.rssmodel import RSSModel

from requests.exceptions import ConnectionError

from django.db.utils import IntegrityError

from threading import Thread
from queue import Queue

CONCURRENT = 50

import django
django.setup()

def do_crawling(q):
    while True:
        site = q.get()
        print("== Coletando: {0} ==\n".format(site.link_rss))
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
                            break
                        if s.status_code == 200 or s.status_code == 301:
                            try:
                                rss_model = RSSModel(coleta.entries[col], s.url, coleta.entries[col].link, site.fk_sites)
                                post = Postagens(titulo=rss_model.titulo,
                                                 link=rss_model.link,
                                                 link_origi=rss_model.link_real,
                                                 texto=rss_model.texto,
                                                 fk_site=rss_model.fk_site,
                                                 fk_imagem=rss_model.imagem_banco)
                                post.save()

                                tags = []
                                for t in rss_model.tags:
                                    try:
                                        db_tag = Tags.objects.get(tag=t)
                                        db_tag.contador += 1
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
                                #print("INTEGRIDADE: UNIQUE - {0}".format(coleta.entries[col].link))
                                pass

                    except Postagens.MultipleObjectsReturned:
                        print("ERRO: Multiplos objetos Retornados - {0}".format(coleta.entries[col].link))
        else:
            print("A consulta não retornou resultados \n")
        print("Coleta Concluida - {0}".format(site.link_rss))
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


