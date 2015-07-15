__author__ = 'nolram'

import operator
import requests

from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from lxml.html.clean import Cleaner

from Crawler.models import Tags, Imagens

class RSSModel:
    def __init__(self, dados, link, link_real, fk_site):
        self.titulo = ""
        self.link = link
        self.link_real = link_real
        self.fk_site = fk_site
        self.texto = ""
        self.imagem_banco = None
        self.tags = []
        self.cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
        self.transformar(dados)

    def transformar(self, dados):
        try:
            self.texto = self.cleaner.clean_html(dados["summary"])
        except Exception:
            self.texto = dados["summary"]
        if "tags" in dados:
            self.add_tags(dados["tags"])
        self.verificar_imagem(dados)
        
    def verificar_imagem(self, dados):
        image_content = NamedTemporaryFile(delete=True)
        if "img" in dados:
            if "src" in dados.img:
                imagem_url = dados.img["src"]
                image_content.write(requests.get(imagem_url).content)
                image_content.flush()
                self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                self.imagem_banco.save()
            elif "url" in dados.img:
                imagem_url = dados.img["url"]
                image_content.write(requests.get(imagem_url).content)
                image_content.flush()
                self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                self.imagem_banco.save()
            elif "href" in dados.img:
                imagem_url = dados.img["href"]
                image_content.write(requests.get(imagem_url).content)
                image_content.flush()
                self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                self.imagem_banco.save()
            elif "link" in dados.img:
                imagem_url = dados.img["link"]
                image_content.write(requests.get(imagem_url).content)
                image_content.flush()
                self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                self.imagem_banco.save()
        elif "media_thumbnail" in dados:
            tmp_media = []
            for j in dados["media_thumbnail"]:
                if "width" in j:
                    tmp_media.append(j)
            sorted_x = sorted(tmp_media, key=operator.itemgetter("width"))
            if len(sorted_x) != 0:
                imagem_url = sorted_x[0]["url"]
            else:
                imagem_url = dados["media_thumbnail"][0]["url"]
            image_content.write(requests.get(imagem_url).content)
            image_content.flush()
            self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
            self.imagem_banco.save()
        elif "links" in dados:
            for li in dados.links:
                if "type" in li:
                    if li.type.find("image") != -1:
                        imagem_url = li.href
                        image_content.write(requests.get(imagem_url).content)
                        image_content.flush()
                        self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                        self.imagem_banco.save()
                        break

    def add_tags(self, tags):
        for tag in tags:
            try:
                db_tag = Tags.objects.get(tag=tag["term"].lower())
                db_tag.contador += 1
                db_tag.save()
                self.tags.append(db_tag)
            except Tags.DoesNotExist:
                db_tag = Tags(tag=tag["term"].lower())
                db_tag.save()
                self.tags.append(db_tag)
