__author__ = 'nolram'

import re
import json
import html
import nltk
import string

class RSSModel:
    def __init__(self, dados, link, link_real, fk_rss):
        self.titulo = dados["title"]
        self.link = link
        self.link_real = link_real
        self.fk_rss = fk_rss
        self.texto = ""
        self.imagem_banco = None
        self.tags = []
        self.limpar_palavras(dados)

    def converter(self, dados):
        if "summary_detail" in dados:
            try:
                tmp = json.loads(dados["summary_detail"])
                if len(tmp["values"]) != 0:
                    self.texto = nltk.clean_html(html.unescape(tmp["values"]))
                else:
                    try:
                        self.texto = nltk.clean_html(html.unescape(dados["summary"]))
                    except Exception:
                        self.texto = html.unescape(dados["summary"])
            except ValueError:
                try:
                    self.texto = nltk.clean_html(html.unescape(dados["summary"]))
                except Exception:
                    self.texto = html.unescape(dados["summary"])
            except Exception:
                try:
                    self.texto = nltk.clean_html(html.unescape(dados["summary"]))
                except Exception:
                    self.texto = html.unescape(dados["summary"])
        else:
            try:
                self.texto = nltk.clean_html(html.unescape(dados["summary"]))
            except Exception:
                self.texto = html.unescape(dados["summary"])

        if "tags" in dados:
            self.add_tags(dados["tags"])

    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(tag["term"].lower())

    def normalizar_palavras(self):
        regex = re.compile('[{0}]'.format(re.escape(string.punctuation)))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        palavras = []
        if len(self.texto) > 0:
            linha = self.texto.replace("\n", " ")
        else:
            linha = self.titulo.replace("\n", " ")
        toks1 = linha.split()
        for t1 in toks1:
            traduzido = regex.sub('', t1)
            toks2 = traduzido.split()
            for t2 in toks2:
                t2s = t2.strip().lower()
                if t2s in stop_words:
                    pass
                else:
                    palavras.append(t2s)
        return palavras

    def coletar_todas_palavras(self, itens):
        palavras = []
        for item in itens:
            for w in item.all_words:
                palavras.append(w)
        return palavras

    def rankear_palavras(self, todas_palavras):
        freq_dist = nltk.FreqDist(w.lower() for w in todas_palavras)
        return freq_dist.keys()[:1000]

