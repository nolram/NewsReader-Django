import operator
import feedparser as fp

from Crawler.models import LinksRSS


class EmComum:
    def __init__(self):
        self.all_links = LinksRSS.objects.all()
        self.zerar_listas()

    def coletar(self):
        for i in self.all_links:
            tmp_parse = fp.parse(i.link_rss)
            if tmp_parse.entries and len(tmp_parse.entries) > 0:
                self.propriedades[i.link_rss] = []
                for j in tmp_parse.entries:
                    for l in j.keys():
                        if l not in self.propriedades[i.link_rss]:
                            self.propriedades[i.link_rss].append(l)
                print("Acessado com sucesso: {}".format(i.link_rss))
            elif tmp_parse.status == 301 and len(tmp_parse.entries) > 0:
                self.propriedades[i.link_rss] = []
                for j in tmp_parse.entries:
                    for l in j.keys():
                        if l not in self.propriedades[i.link_rss]:
                            self.propriedades[tmp_parse.href].append(l)
                print("Link: {} - Movido para: {}".format(i.link_rss, tmp_parse.href))
                self.movidos.append(tmp_parse.href)
            else:
                print("Página {} retornou um erro".format(i.link_rss))
                self.erros[i.link_rss] = i.link_rss if not tmp_parse.bozo_exception else tmp_parse.bozo_exception

    def analisar(self):
        for a, c in self.propriedades.items():
            for b in c:
		if b in self.em_comum:
		    self.em_comum[b] += 1
		else:
		    self.em_comum[b] = 1
	self.sorted_x = sorted(self.em_comum.items(), key=operator.itemgetter(1), reverse=True)
    
    def zerar_listas(self):
        self.propriedades = {}
        self.movidos = []
        self.erros = {}
        self.em_comum = {}
        self sorted_x = []
        
