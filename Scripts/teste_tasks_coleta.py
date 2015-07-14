__author__ = 'nolram'

import requests
import feedparser as fp

from Crawler.models import LinksRSS, Postagens, Tags, TagsPostagens, Imagens
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from lxml.html.clean import Cleaner

def do_crawler():
    print("Coletando postagens")
    sites = LinksRSS.objects.all()
    cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
    for site in sites:
        coleta = fp.parse(site.link_rss)
        print(site.link_rss)
        if "entries" in coleta:
            for col in coleta.entries:
                try:
                    post = Postagens.objects.get(link_origi=col.link)
                except Postagens.DoesNotExist:
                    s = requests.get(col.link)
                    if s.status_code == 200 or s.status_code == 301:
                        link = s.url
                        try:
                            texto = cleaner.clean_html(col["summary"])
                        except Exception:
                            texto = col["summary"]
                        valores = {
                            "titulo": col["title"],
                            "texto": texto,
                            "fk_site": site.fk_sites,
                            "link_origi": col.link
                        }
                        image_content = NamedTemporaryFile(delete=True)
                        if "img" in col:
                            if "src" in col.img:
                                image_content.write(requests.get(col.img["src"]).content)
                                image_content.flush()
                                imga = Imagens(img_cover=File(image_content), img_link_orig=col.img["src"])
                                imga.save()
                                valores["fk_imagem"] = imga
                            elif "url" in col.img:
                                image_content.write(requests.get(col.img["url"]).content)
                                image_content.flush()
                                imga = Imagens(img_cover=File(image_content), img_link_orig=col.img["url"])
                                imga.save()
                                valores["fk_imagem"] = imga
                            elif "href" in col.img:
                                image_content.write(requests.get(col.img["href"]).content)
                                image_content.flush()
                                imga = Imagens(img_cover=File(image_content), img_link_orig=col.img["href"])
                                imga.save()
                                valores["fk_imagem"] = imga
                            elif "link" in col.img:
                                image_content.write(requests.get(col.img["link"]).content)
                                image_content.flush()
                                imga = Imagens(img_cover=File(image_content), img_link_orig=col.img["link"])
                                imga.save()
                                valores["fk_imagem"] = imga
                        elif "media_thumbnail" in col:
                            image_content.write(requests.get(col.media_thumbnail[0]["url"]).content)
                            image_content.flush()
                            imga = Imagens(img_cover=File(image_content),
                                           img_link_orig=col.media_thumbnail[0]["url"])
                            imga.save()
                            valores["fk_imagem"] = imga
                        elif "links" in col:
                            for li in col.links:
                                if "type" in li:
                                    if li.type.find("image") != -1:
                                        image_content.write(requests.get(li.href).content)
                                        image_content.flush()
                                        imga = Imagens(img_cover=File(image_content), img_link_orig=li.href)
                                        imga.save()
                                        valores["fk_imagem"] = imga

                        post, existe = Postagens.objects.get_or_create(link=link, defaults=valores)

                        if not existe and "tags" in col:
                            tags = {}
                            for tag in col["tags"]:
                                try:
                                    db_tag = Tags.objects.get(tag=tag["term"].lower())
                                    db_tag.contador += 1
                                    db_tag.save()
                                    tpos, check = TagsPostagens.objects.get_or_create(fk_tag=db_tag, fk_postagem=post)
                                except Tags.DoesNotExist:
                                    db_tag = Tags(tag=tag["term"].lower())
                                    db_tag.save()
                                    tpos, check = TagsPostagens.objects.get_or_create(fk_tag=db_tag, fk_postagem=post)
        else:
            print("A consulta não retornou resultados")

    print("Coleta Concluida")
