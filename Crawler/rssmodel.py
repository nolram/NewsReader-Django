__author__ = 'nolram'

import json
import html
import operator
import requests

from dateutil import parser

from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.utils import timezone
from django.db.utils import IntegrityError

from lxml.html.clean import Cleaner

from Crawler.models import Imagens

SEMANAS = {"Seg": "Mon",
           "Ter": "Tue",
           "Qua": "Wed",
           "Qui": "Thu",
           "Sex": "Fri",
           "Sab": "Sat",
           "Dom": "Sun"}

MESES = {"Jan": "Jan",
         "Fev": "Feb",
         "Mar": "Mar",
         "Abr": "Apr",
         "Mai": "May",
         "Jun": "Jun",
         "Jul": "Jul",
         "Ago": "Aug",
         "Set": "Sep",
         "Out": "Oct",
         "Nov": "Nov",
         "Dez": "Dec"}

SALVAR_IMAGEM = True


class RSSModel:
    def __init__(self, dados, link, link_real, fk_rss):
        self.titulo = dados["title"]
        self.link = link
        self.link_real = link_real
        self.fk_rss = fk_rss
        self.texto = ""
        self.imagem_banco = None
        self.data_publicacao = None
        self.tags = []
        self.cleaner = Cleaner(kill_tags=['script', 'style'], remove_unknown_tags=True)
        self.converter(dados)

    def converter(self, dados):
        if "summary_detail" in dados:
            try:
                tmp = json.loads(dados["summary_detail"])
                if len(tmp["values"]) != 0:
                    self.texto = self.cleaner.clean_html(html.unescape(tmp["values"]))
                else:
                    try:
                        self.texto = self.cleaner.clean_html(html.unescape(dados["summary"]))
                    except Exception:
                        self.texto = html.unescape(dados["summary"])
            except ValueError:
                try:
                    self.texto = self.cleaner.clean_html(html.unescape(dados["summary"]))
                except Exception:
                    self.texto = html.unescape(dados["summary"])
            except Exception:
                try:
                    self.texto = self.cleaner.clean_html(html.unescape(dados["summary"]))
                except Exception:
                    self.texto = html.unescape(dados["summary"])
        else:
            try:
                self.texto = self.cleaner.clean_html(html.unescape(dados["summary"]))
            except Exception:
                self.texto = html.unescape(dados["summary"])

        if "tags" in dados:
            self.add_tags(dados["tags"])

        if "published" in dados and dados["published"] is not None:
            try:
                self.data_publicacao = parser.parse(dados["published"])
            except ValueError:
                try:
                    data = self.converter_data(dados["published"])
                    if data is not None:
                        self.data_publicacao = parser.parse(data)
                    else:
                        self.data_publicacao = timezone.now()
                except ValueError:
                    print("Falha ao converter: {0}".format(self.converter_data(dados["published"])))
                    self.data_publicacao = timezone.now()
        else:
            self.data_publicacao = timezone.now()

        self.verificar_imagem(dados)
        
    def verificar_imagem(self, dados):
        try:
            image_content = NamedTemporaryFile(delete=True)
            if "img" in dados:
                imagem_url = None
                if "src" in dados.img:
                    imagem_url = dados.img["src"]
                elif "url" in dados.img:
                    imagem_url = dados.img["url"]
                elif "href" in dados.img:
                    imagem_url = dados.img["href"]
                elif "link" in dados.img:
                    imagem_url = dados.img["link"]
                if SALVAR_IMAGEM is True and imagem_url is not None:
                    image_content.write(requests.get(imagem_url).content)
                    image_content.flush()
                    self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                    self.imagem_banco.save()
                elif imagem_url is not None:
                    self.imagem_banco = Imagens(img_link_orig=imagem_url)
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
                if SALVAR_IMAGEM:
                    image_content.write(requests.get(imagem_url).content)
                    image_content.flush()
                    self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                    self.imagem_banco.save()
                else:
                    self.imagem_banco = Imagens(img_link_orig=imagem_url)
                    self.imagem_banco.save()
            elif "links" in dados:
                for li in dados.links:
                    if "type" in li:
                        if li.type.find("image") != -1:
                            imagem_url = li.href
                            if SALVAR_IMAGEM:
                                image_content.write(requests.get(imagem_url).content)
                                image_content.flush()
                                self.imagem_banco = Imagens(img_cover=File(image_content), img_link_orig=imagem_url)
                                self.imagem_banco.save()
                            else:
                                self.imagem_banco = Imagens(img_link_orig=imagem_url)
                                self.imagem_banco.save()
                            break
        except IntegrityError:
            self.imagem_banco = None

    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(tag["term"].lower())

    def converter_data(self, data):
        # Seg, 27 Jul 2015 12:05:00 -0300
        # Mon, 03 Ago 2015 15:54:00 -0300
        data_modificada = None
        semana = data[:3]
        mes = data[8:11]
        if mes in MESES:
            data_modificada = data.replace(mes, MESES[mes])
            if semana in SEMANAS:
                data_modificada = data_modificada.replace(semana, SEMANAS[semana])
            else:
                print("Semana não encontrada: {0}".format(semana))
                data_modificada = None
        else:
            print("Mês não encontrado: {0}".format(mes))
            data_modificada = None

        return data_modificada
