__author__ = '@nolram'
from Crawler.models import Sites, Categorias, SitesCategorias, LinksRSS


def add_pages():
    sites = [
        {"titulo": "Zero Hora", "descricao": "Zero Hora", "link": "http://zh.clicrbs.com.br/rs/", "idioma": "pt-BR"},
        {"titulo": "UOL", "descricao": "UOL", "link": "http://www.uol.com.br/", "idioma": "pt-BR"},
        {"titulo": "Terra", "descricao": "Terra", "link": "http://www.terra.com.br/", "idioma": "pt-BR"},
        {"titulo": "Globo", "descricao": "Globo", "link": "http://www.globo.com/", "idioma": "pt-BR"},
        {"titulo": "Estadão", "descricao": "Estadão", "link": "http://www.estadao.com.br/", "idioma": "pt-BR"},
        {"titulo": "Folha de São Paulo", "descricao": "Folha de São Paulo", "link": "http://www.folha.uol.com.br/",
         "idioma": "pt-BR"},
        {"titulo": "IG", "descricao": "IG", "link": "http://www.ig.com.br/", "idioma": "pt-BR"},
        {"titulo": "R7", "descricao": "R7", "link": "http://www.r7.com/", "idioma": "pt-BR"},
        {"titulo": "Yahoo! Notícias", "descricao": "Yahoo! Notícias", "link": "https://br.noticias.yahoo.com",
         "idioma": "pt-BR"},
        {"titulo": "MSN", "descricao": "MSN", "link": "http://www.msn.com/pt-br", "idioma": "pt-BR"},
        {"titulo": "G1", "descricao": "G1", "link": "http://g1.globo.com/", "idioma": "pt-BR"},
        {"titulo": "The New York Times", "descricao": "The New York Times", "link": "http://www.nytimes.com/",
         "idioma": "en-US"},
        {"titulo": "BBC UK", "descricao": "BBC UK", "link": "http://www.bbc.com/", "idioma": "en"},
        {"titulo": "Globo Esporte", "descricao": "Globo Esporte", "link": "http://globoesporte.globo.com/",
         "idioma": "pt-BR"},
        {"titulo": "iMasters", "descricao": "iMasters", "link": "http://imasters.com.br/", "idioma": "pt-BR"},
        {"titulo": "O Globo", "descricao": "O Globo", "link": "http://oglobo.globo.com/", "idioma": "pt-BR"},
        {"titulo": "Tecmundo", "descricao": "Tecmundo", "link": "http://www.tecmundo.com.br/", "idioma": "pt-BR"},
        {"titulo": "Gizmodo BR", "descricao": "Gizmodo BR", "link": "http://gizmodo.uol.com.br/",
         "idioma": "pt-BR"},
        {"titulo": "Jovem Nerd", "descricao": "Jovem Nerd", "link": "http://jovemnerd.com.br/", "idioma": "pt-BR"},
        {"titulo": "Lancenet", "descricao": "Lancenet", "link": "http://www.lancenet.com.br/", "idioma": "pt-BR"},
        {"titulo": "Techtudo", "descricao": "Techtudo", "link": "http://www.techtudo.com.br/", "idioma": "pt-BR"},
        {"titulo": "Olhar Digital", "descricao": "Olhar Digital", "link": "http://olhardigital.uol.com.br/",
         "idioma": "pt-BR"},
        {"titulo": "IEEE Spectrum", "descricao": "IEEE Spectrum", "link": "http://spectrum.ieee.org/",
         "idioma": "pt-BR"},
    ]
    sites_banco = []
    for site in sites:
        pagina = Sites(titulo=site["tiulo"], descricao=site["descricao"], link=site["link"], idioma=site["idioma"])
        pagina.save()
        sites_banco.append({site["titulo"].lower(): pagina})
