__author__ = '@nolram'

import os
import django

from Crawler.models import Sites, Categorias, RSSCategorias, LinksRSS


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

django.setup()

class PrimeiraAdicao:

    def __init__(self):
        arq_sites = open(os.path.join(BASE_DIR, "Crawler", "arquivos_iniciais")+"/links_sites", "r")
        self.sites = [i.replace("\n", "").split(",") for i in arq_sites.readlines()]
        self.sites_banco = {}

        arq_rss = open(os.path.join(BASE_DIR, "Crawler", "arquivos_iniciais")+"/links_rss", "r")
        self.links_rss = [i.replace("\n", "").split(",") for i in arq_rss.readlines()]
        self.rss_banco = []

        arq_cat = open(os.path.join(BASE_DIR, "Crawler", "arquivos_iniciais")+"/categorias.txt", "r")
        self.cate = [i.replace("\n", "") for i in arq_cat.readlines()]
        self.cat_dict = {}

        arq_rss.close()
        arq_sites.close()

    def add_pages(self):
        print("Adicionando categorias...")
        for cat in self.cate:
            categoria = Categorias(categoria=cat)
            categoria.save()
            self.cat_dict[cat] = categoria
        print("Adicionando os sites...")
        for site in self.sites:
            pagina = Sites(titulo=site[0], descricao=site[1], link=site[2], idioma=site[3])
            pagina.save()
            self.sites_banco[site[0].lower()] = pagina
        print("Adicionando os links RSS")
        for rss in self.links_rss:
            if self.sites_banco.get(rss[0]):
                rss_pagina = LinksRSS(fk_sites=self.sites_banco.get(rss[0]), link_rss=rss[1])
                rss_pagina.save()
                cat_rss = rss[2].replace("{", "").replace("}", "").split(":")
                for c in cat_rss:
                    if c in self.cat_dict:
                        ob_rss_cat = RSSCategorias(fk_rss=rss_pagina,fk_categoria=self.cat_dict[c])
                        ob_rss_cat.save()

        print("Término do algoritmo...")
