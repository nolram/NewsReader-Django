from __future__ import absolute_import
from celery.backends.database import retry
from django.db import OperationalError

__author__ = 'marlon'

import feedparser as fp

from celery import shared_task, task
from celery.utils.log import get_task_logger

from Crawler.models import Categorias, LinksRSS, Postagens, Sites, Tags, TagsPostagens
from django.core.exceptions import ObjectDoesNotExist


logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@task(name='tasks.do_crawler')
def do_crawler():
    logger.info("Coletando postagens")
    try:
        sites = LinksRSS.objects.all()
        for site in sites:
            coleta = fp.parse(site.link_rss)
            for col in coleta["items"]:
                post, check = Postagens.objects.get_or_create(link=col["wfw_commentrss"].replace("feed/", ""),
                                                                defaults={"titulo": col["title"],
                                                                 "texto": col["summary"],
                                                                 "fk_site": site.fk_sites})
                if not check:
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

    except Exception as exce:
        raise retry(exc=exce)

    logger.info("Coleta Concluida")
