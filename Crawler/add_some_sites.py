__author__ = '@nolram'

import os

from Crawler.models import Sites, Categorias, SitesCategorias, LinksRSS


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class PrimeiraAdicao:

    def __init__(self):
        arq_sites = open(os.path.join(BASE_DIR, "Crawler", "arquivos_iniciais")+"/links_sites", "r")
        self.sites = [i.replace("\n", "").split(",") for i in arq_sites.readlines()]
        self.sites_banco = {}

        arq_rss = open(os.path.join(BASE_DIR, "Crawler", "arquivos_iniciais")+"/links_rss", "r")
        self.links_rss = [i.replace("\n", "").split(",") for i in arq_rss.readlines()]
        self.rss_banco = []

        arq_rss.close()
        arq_sites.close()

    def add_pages(self):
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

        print("Término do algoritmo...")
