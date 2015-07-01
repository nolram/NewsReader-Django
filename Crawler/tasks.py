from __future__ import absolute_import
from celery.backends.database import retry
from django.db import OperationalError

__author__ = 'marlon'

import feedparser as fp

from celery import shared_task, task
from celery.utils.log import get_task_logger

from Crawler.models import Categorias, LinksRSS, Postagens, Sites, Tags, TagsPostagens
from django.core.exceptions import ObjectDoesNotExist

from lxml.html.clean import clean_html, Cleaner

logger = get_task_logger(__name__)


@task(name='tasks.do_crawler')
def do_crawler():
    logger.info("Coletando postagens")
    try:
        sites = LinksRSS.objects.all()
        for site in sites:
            try:
                coleta = fp.parse(site.link_rss)
                if len(coleta.entries) > 0:
                    for col in coleta.entries:
                        if "wfw_commentrss" in col:
                            post, check = Postagens.objects.get_or_create(link=col["wfw_commentrss"].replace("feed/", ""),
                                                                            defaults={"titulo": col["title"],
                                                                             "texto": col["summary"],
                                                                             "fk_site": site.fk_sites})
                        elif "feedburner_origlink" in col and isinstance(col["feedburner_origlink"], str):
                            post, check = Postagens.objects.get_or_create(link=col["feedburner_origlink"],
                                                                            defaults={"titulo": col["title"],
                                                                             "texto": col["summary"],
                                                                             "fk_site": site.fk_sites})
                        else:
                            post, check = Postagens.objects.get_or_create(link=col["link"],
                                                                            defaults={"titulo": col["title"],
                                                                             "texto": col["summary"],
                                                                             "fk_site": site.fk_sites})
                            teste = Cleaner()
                        if not check:
                            if "tags" in col:
                                for tag in col["tags"]:
                                    try:
                                        db_tag = Tags.objects.get(tag=tag["term"].lower())
                                        db_tag.contador += 1
                                        db_tag.save()
                                    except ObjectDoesNotExist:
                                        db_tag = Tags(tag=tag["term"].lower())
                                        db_tag.save()
                                    tpos = TagsPostagens(fk_tag=db_tag, fk_postagem=post)
                                    tpos.save()
                else:
                    logger.info("A consulta não retornou resultados")
            except Exception:
                logger.info("Erro na coleta da página: {0}".format(site.link_rss))

    except Exception as exce:
        logger.info("Erro: ")

    logger.info("Coleta Concluida")
