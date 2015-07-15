__author__ = 'nolram'

import requests
import feedparser as fp

from Crawler.models import LinksRSS, Postagens, Tags, TagsPostagens, Imagens
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from lxml.html.clean import Cleaner

from requests.exceptions import ConnectionError

from Crawler.rssmodel import RSSModel

def do_crawler():
    import django
    django.setup()
    print("Coletando postagens")
    sites = LinksRSS.objects.all()
    for site in sites:
        coleta = fp.parse(site.link_rss)
        print(site.link_rss)
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
                            rss_model = RSSModel(coleta.entries[col], s.url, coleta.entries[col].link, site.fk_sites)
                            post = Postagens(titulo=rss_model.link,
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
        else:
            print("A consulta não retornou resultados")

    print("Coleta Concluida")
