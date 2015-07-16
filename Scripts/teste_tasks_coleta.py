__author__ = 'nolram'

import time
import requests
import feedparser as fp

from Crawler.models import LinksRSS, Postagens, TagsPostagens

from requests.exceptions import ConnectionError

from Crawler.rssmodel import RSSModel

def do_crawler():
    tempo1 = time.time()
    import django
    django.setup()
    print("Coletando postagens \n")
    sites = LinksRSS.objects.all()
    tempo2 = time.time()
    print("Tempo para pesquisar todos os links - {0} \n".format(str(tempo2-tempo1)))
    for site in sites:
        tempo3 = time.time()
        coleta = fp.parse(site.link_rss)
        tempo4 = time.time()
        print("=RSS site {0}: {1}".format(site.link_rss, str(tempo4-tempo3)))
        if "entries" in coleta:
            tempo3 = time.time()
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
                            rss_model = RSSModel(coleta.entries[col], s.url, coleta.entries[col].link, site.fk_sites)
                            post = Postagens(titulo=rss_model.titulo,
                                             link=rss_model.link,
                                             link_origi=rss_model.link_real,
                                             texto=rss_model.texto,
                                             fk_site=rss_model.fk_site,
                                             fk_imagem=rss_model.imagem_banco)
                            post.save()

                            for tag in rss_model.tags:
                                try:
                                    TagsPostagens.objects.get(fk_tag=tag, fk_postagem=post)
                                except TagsPostagens.DoesNotExist:
                                    tpos = TagsPostagens(fk_tag=tag, fk_postagem=post)
                                    tpos.save()
            tempo4 = time.time()
            print("===Banco de Dados: {0} \n".format(str(tempo4-tempo3)))
        else:
            print("A consulta não retornou resultados \n")
    tempo5 = time.time()
    print("Tempo total de Crawling: {0} \n".format(str(tempo5-tempo1)))
    print("Coleta Concluida")
