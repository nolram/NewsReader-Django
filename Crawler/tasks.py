from __future__ import absolute_import
from celery.backends.database import retry
from django.db import OperationalError

__author__ = 'marlon'

import requests
import feedparser as fp

from celery import task
from celery.utils.log import get_task_logger

from Crawler.models import LinksRSS, Postagens, Tags, TagsPostagens, Imagens

from lxml.html.clean import Cleaner

from django.core.files.images import ImageFile

logger = get_task_logger(__name__)


@task(name='tasks.do_crawler')
def do_crawler():
    logger.info("Coletando postagens")
    try:
        sites = LinksRSS.objects.all()
        cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
        for site in sites:
            try:
                coleta = fp.parse(site.link_rss)
                if "entries" in coleta:
                    for col in coleta.entries:
                        s = requests.get(col.link)
                        if s.status_code == 200 or s.status_code == 301:
                            link = s.url
                            texto = cleaner.clean_html(col["summary"])
                            valores = {
                                "titulo": col["title"],
                                "texto": texto,
                                "fk_site": site.fk_sites
                            }
                            if "img" in col:
                                if "src" in col.img:
                                    image_content = ImageFile(requests.get(col.img.src).content)
                                    imga = Imagens(img_cover=image_content, img_link_orig=col.img.src)
                                    imga.save()
                                    valores["fk_imagem"] = imga
                                elif "url" in col.img:
                                    image_content = ImageFile(requests.get(col.img.url).content)
                                    imga = Imagens(img_cover=image_content, img_link_orig=col.img.url)
                                    imga.save()
                                    valores["fk_imagem"] = imga
                                elif "href" in col.img:
                                    image_content = ImageFile(requests.get(col.img.href).content)
                                    imga = Imagens(img_cover=image_content, img_link_orig=col.img.href)
                                    imga.save()
                                    valores["fk_imagem"] = imga
                                elif "link" in col.img:
                                    image_content = ImageFile(requests.get(col.img.link).content)
                                    imga = Imagens(img_cover=image_content, img_link_orig=col.img.link)
                                    imga.save()
                                    valores["fk_imagem"] = imga
                            elif "media_thumbnail" in col:
                                image_content = ImageFile(requests.get(col.media_thumbnail[0].url).content)
                                imga = Imagens(img_cover=image_content, img_link_orig=col.img.src)
                                imga.save()
                                valores["fk_imagem"] = imga
                            elif "links" in col:
                                for li in col.links:
                                    if "type" in li:
                                        if li.type.find("image") != -1:
                                            image_content = ImageFile(requests.get(li.href).content)
                                            imga = Imagens(img_cover=image_content, img_link_orig=col.img.src)
                                            imga.save()
                                            valores["fk_imagem"] = imga

                            post, existe = Postagens.objects.get_or_create(link=link, defaults=valores)
                            if not existe:
                                if "tags" in col:
                                    for tag in col["tags"]:
                                        try:
                                            db_tag = Tags.objects.get(tag=tag["term"].lower())
                                            db_tag.contador += 1
                                            db_tag.save()
                                        except Tags.DoesNotExist:
                                            db_tag = Tags(tag=tag["term"].lower())
                                            db_tag.save()
                                        try:
                                            tpos = TagsPostagens.objects.get(fk_tag=db_tag, fk_postagem=post)
                                        except TagsPostagens.DoesNotExist:
                                            tpos = TagsPostagens(fk_tag=db_tag, fk_postagem=post)
                                            tpos.save()
                else:
                    logger.info("A consulta não retornou resultados")
            except Exception:
                logger.info("Erro na coleta da página: {0}".format(site.link_rss))

    except Exception as exce:
        logger.info("Erro: ")

    logger.info("Coleta Concluida")
