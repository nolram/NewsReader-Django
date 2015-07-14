Python 3.4.2 (default, Jan 12 2015, 12:13:20) 
[GCC 4.9.2 20150107 (Red Hat 4.9.2-5)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from Crawler.models import Categorias, LinksRSS, Postagens, Sites, Tags, TagsPostagens
>>> all_links = LinksRSS.objects.all()
>>> propriedades = {}
>>> movidos = []
>>> erros = []
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		propriedades[i.link_rss] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
	elif tmp_parse.status == 301 and len(tmp_parse.entries) > 0:
		propriedades[tmp_parse.href] = tmp_parse.entries[0].keys()
		print("Link: {} - Movido para: {}".format(i.link_rss, tmp_parse.href))
		movidos.append(tmp_parse.href)
	else:
		print("Página {} retornou um erro".format(i.link_rss))
		erros.append(i.link_rss)

		
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    tmp_parse = fp.parse(i.link_rss)
NameError: name 'fp' is not defined
>>> import feedparser as fp
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		propriedades[i.link_rss] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
	elif tmp_parse.status == 301 and len(tmp_parse.entries) > 0:
		propriedades[tmp_parse.href] = tmp_parse.entries[0].keys()
		print("Link: {} - Movido para: {}".format(i.link_rss, tmp_parse.href))
		movidos.append(tmp_parse.href)
	else:
		print("Página {} retornou um erro".format(i.link_rss))
		erros.append(i.link_rss)

		
Página http://www.baixaki.com.br/rss/tecnologia.xml retornou um erro
Acessado com sucesso: http://tecnologia.uol.com.br/ultnot/index.xml
Acessado com sucesso: http://feeds.feedburner.com/IeeeSpectrum
Acessado com sucesso: http://zh.clicrbs.com.br/rs/ultimas-noticias-rss/
Acessado com sucesso: http://zh.clicrbs.com.br/rs/esportes/ultimas-noticias-rss/
Acessado com sucesso: http://zh.clicrbs.com.br/rs/noticias/economia/ultimas-noticias-rss/
Acessado com sucesso: http://rss.uol.com.br/feed/noticias.xml
Acessado com sucesso: http://feeds.folha.uol.com.br/emcimadahora/rss091.xml
Acessado com sucesso: http://ig.ultimosegundo.feedsportal.com/c/33511/f/637143/index.rss
Acessado com sucesso: http://noticias.r7.com/brasil/feed.xml
Acessado com sucesso: https://br.noticias.yahoo.com/rss/brasil
Acessado com sucesso: http://g1.globo.com/dynamo/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/brasil/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/concursos-e-emprego/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/economia/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/educacao/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/loterias/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/mundo/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/musica/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/tecnologia/rss2.xml
Acessado com sucesso: http://feeds.bbci.co.uk/news/rss.xml
Acessado com sucesso: http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss
Acessado com sucesso: http://imasters.com.br/feed/
Acessado com sucesso: http://feeds.feedburner.com/gizmodobr
Acessado com sucesso: http://www.lancenet.com.br/rss/latest/
Acessado com sucesso: http://feeds.feedburner.com/techtudo
Acessado com sucesso: http://omelete.com.br.feedsportal.com/cinema
Acessado com sucesso: http://omelete.com.br.feedsportal.com/quadrinhos
Acessado com sucesso: http://omelete.com.br.feedsportal.com/series-e-tv
Acessado com sucesso: http://omelete.com.br.feedsportal.com/games
Acessado com sucesso: http://omelete.com.br.feedsportal.com/rss
Acessado com sucesso: http://esporte.uol.com.br/ultimas/index.xml
Acessado com sucesso: http://rss.uol.com.br/feed/economia.xml
Acessado com sucesso: http://feeds.wired.com/wired/index
Acessado com sucesso: http://www.wired.com/category/business/feed/
Acessado com sucesso: http://www.wired.com/category/design/feed/
Acessado com sucesso: http://www.wired.com/category/underwire/feed/
Acessado com sucesso: http://www.wired.com/category/gear/feed/
Acessado com sucesso: http://www.wired.com/category/reviews/feed/
Acessado com sucesso: http://www.wired.com/category/science/feed/
Acessado com sucesso: http://www.wired.com/category/science/science-blogs/feed/
Acessado com sucesso: http://www.wired.com/category/threatlevel/feed/
Acessado com sucesso: http://feeds.cnevids.com/brand/wired.mrss
Acessado com sucesso: http://www.wired.com/category/photo/feed/
Acessado com sucesso: http://www.theverge.com/rss/index.xml
Acessado com sucesso: http://www.theverge.com/tech/rss/index.xml
Acessado com sucesso: http://www.theverge.com/apple/rss/index.xml
Acessado com sucesso: http://www.theverge.com/google/rss/index.xml
Acessado com sucesso: http://www.theverge.com/microsoft/rss/index.xml
Acessado com sucesso: http://feeds.reuters.com/news/artsculture
Acessado com sucesso: http://feeds.reuters.com/reuters/businessNews
Acessado com sucesso: http://feeds.reuters.com/reuters/entertainment
Acessado com sucesso: http://feeds.reuters.com/news/wealth
Acessado com sucesso: http://feeds.reuters.com/reuters/scienceNews
Acessado com sucesso: http://feeds.reuters.com/reuters/technologyNews
Acessado com sucesso: http://feeds.reuters.com/reuters/topNews
Acessado com sucesso: http://feeds.reuters.com/Reuters/worldNews
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Noticias
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Mercados
Acessado com sucesso: http://feeds.feedburner.com/Exame-Negocios
Acessado com sucesso: http://feeds.feedburner.com/Exame-Economia
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Marketing
Acessado com sucesso: http://feeds.feedburner.com/Exame-Tecnologia
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Marketing
Acessado com sucesso: http://feeds.feedburner.com/Exame-Gestao
Acessado com sucesso: http://feeds.feedburner.com/Exame-GaleriaCiencia
Acessado com sucesso: http://revistagalileu.globo.com/rss/ultimas/feed.xml
Acessado com sucesso: http://www.bbc.com/portuguese/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/brasil/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/internacional/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/economia/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/saude/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/ciencia_e_tecnologia/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/cultura/index.xml
>>> erros
['http://www.baixaki.com.br/rss/tecnologia.xml']
>>> movidos
[]
>>> em_comum = {}
>>> propriedades.items()[0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    propriedades.items()[0]
TypeError: 'dict_items' object does not support indexing
>>> propriedades.i()[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    propriedades.i()[0]
AttributeError: 'dict' object has no attribute 'i'
>>> propriedades.items()
dict_items([('http://omelete.com.br.feedsportal.com/cinema', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'published_parsed'])), ('http://ig.ultimosegundo.feedsportal.com/c/33511/f/637143/index.rss', dict_keys(['title_detail', 'link', 'links', 'guidislink', 'summary_detail', 'id', 'summary', 'published', 'published_parsed', 'title'])), ('http://feeds.reuters.com/reuters/businessNews', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'published', 'feedburner_origlink', 'summary', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://www.bbc.com/portuguese/topicos/ciencia_e_tecnologia/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://feeds.feedburner.com/gizmodobr', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'link', 'wfw_commentrss', 'content', 'slash_comments', 'feedburner_origlink', 'published_parsed', 'summary'])), ('http://zh.clicrbs.com.br/rs/esportes/ultimas-noticias-rss/', dict_keys(['title_detail', 'tags', 'links', 'summary', 'published', 'credit', 'title', 'summary_detail', 'media_content', 'link', 'media_credit', 'content', 'published_parsed'])), ('http://g1.globo.com/dynamo/brasil/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://www.theverge.com/tech/rss/index.xml', dict_keys(['title_detail', 'authors', 'updated', 'links', 'guidislink', 'id', 'author', 'summary', 'published', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])), ('http://tecnologia.uol.com.br/ultnot/index.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'published_parsed', 'title'])), ('http://www.bbc.com/portuguese/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://feeds.feedburner.com/techtudo', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'feedburner_origlink', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://www.wired.com/category/photo/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://feeds.feedburner.com/Exame-Tecnologia', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://www.wired.com/category/business/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://g1.globo.com/dynamo/loterias/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://g1.globo.com/dynamo/tecnologia/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://g1.globo.com/dynamo/concursos-e-emprego/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://zh.clicrbs.com.br/rs/noticias/economia/ultimas-noticias-rss/', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://feeds.cnevids.com/brand/wired.mrss', dict_keys(['title_detail', 'href', 'links', 'guidislink', 'id', 'tags', 'summary', 'content_id', 'title', 'cne_contentid', 'published', 'summary_detail', 'media_content', 'link', 'media_keywords', 'media_thumbnail', 'media_player', 'content', 'published_parsed', 'cne_seotitle'])), ('http://www.theverge.com/apple/rss/index.xml', dict_keys(['title_detail', 'authors', 'updated', 'links', 'guidislink', 'id', 'author', 'summary', 'published', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])), ('http://omelete.com.br.feedsportal.com/rss', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'published_parsed'])), ('http://feeds.feedburner.com/EXAME-Noticias', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://www.bbc.com/portuguese/topicos/cultura/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://feeds.feedburner.com/EXAME-Marketing', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://feeds.feedburner.com/Exame-Economia', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://feeds.bbci.co.uk/news/rss.xml', dict_keys(['title_detail', 'href', 'links', 'guidislink', 'id', 'summary', 'published', 'title', 'summary_detail', 'link', 'media_thumbnail', 'published_parsed'])), ('http://zh.clicrbs.com.br/rs/ultimas-noticias-rss/', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://g1.globo.com/dynamo/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://feeds.feedburner.com/IeeeSpectrum', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'updated', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'media_content', 'link', 'media_thumbnail', 'href', 'updated_parsed', 'content', 'published_parsed', 'feedburner_origlink'])), ('http://www.wired.com/category/design/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://omelete.com.br.feedsportal.com/series-e-tv', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'published_parsed'])), ('http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://feeds.reuters.com/reuters/technologyNews', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'published', 'feedburner_origlink', 'summary', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://www.wired.com/category/science/science-blogs/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://feeds.reuters.com/news/wealth', dict_keys(['title_detail', 'summary', 'links', 'guidislink', 'published', 'feedburner_origlink', 'tags', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://www.bbc.com/portuguese/topicos/brasil/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://www.theverge.com/google/rss/index.xml', dict_keys(['title_detail', 'authors', 'updated', 'links', 'guidislink', 'id', 'author', 'summary', 'published', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])), ('http://www.theverge.com/rss/index.xml', dict_keys(['title_detail', 'authors', 'updated', 'links', 'guidislink', 'id', 'author', 'summary', 'published', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])), ('http://feeds.wired.com/wired/index', dict_keys(['title_detail', 'authors', 'tags', 'links', 'guidislink', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed'])), ('http://g1.globo.com/dynamo/economia/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('https://br.noticias.yahoo.com/rss/brasil', dict_keys(['title_detail', 'link', 'links', 'source', 'summary_detail', 'id', 'summary', 'published', 'published_parsed', 'title', 'guidislink'])), ('http://esporte.uol.com.br/ultimas/index.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'title'])), ('http://feeds.feedburner.com/EXAME-Mercados', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://feeds.feedburner.com/Exame-Gestao', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://rss.uol.com.br/feed/noticias.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'published_parsed', 'title'])), ('http://feeds.reuters.com/news/artsculture', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'id', 'feedburner_origlink', 'summary', 'published', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://www.theverge.com/microsoft/rss/index.xml', dict_keys(['title_detail', 'authors', 'updated', 'links', 'guidislink', 'id', 'author', 'summary', 'published', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])), ('http://imasters.com.br/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'id', 'author', 'tags', 'published', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'content', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://feeds.reuters.com/reuters/scienceNews', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'published', 'feedburner_origlink', 'summary', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://feeds.reuters.com/reuters/topNews', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'published', 'feedburner_origlink', 'summary', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://www.wired.com/category/science/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://www.bbc.com/portuguese/topicos/economia/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://rss.uol.com.br/feed/economia.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'published_parsed', 'title'])), ('http://www.wired.com/category/reviews/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://www.lancenet.com.br/rss/latest/', dict_keys(['title_detail', 'links', 'guidislink', 'published', 'summary', 'id', 'title', 'summary_detail', 'link', 'img', 'content', 'figcaption', 'published_parsed', 'figure'])), ('http://feeds.reuters.com/reuters/entertainment', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'published', 'feedburner_origlink', 'summary', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://www.wired.com/category/underwire/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://www.wired.com/category/threatlevel/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://noticias.r7.com/brasil/feed.xml', dict_keys(['title_detail', 'authors', 'summary', 'links', 'guidislink', 'published', 'author', 'updated', 'id', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])), ('http://omelete.com.br.feedsportal.com/quadrinhos', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'published_parsed'])), ('http://feeds.reuters.com/Reuters/worldNews', dict_keys(['title_detail', 'tags', 'links', 'guidislink', 'published', 'feedburner_origlink', 'summary', 'id', 'title', 'summary_detail', 'link', 'published_parsed'])), ('http://omelete.com.br.feedsportal.com/games', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'summary', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'published_parsed'])), ('http://www.wired.com/category/gear/feed/', dict_keys(['title_detail', 'authors', 'links', 'guidislink', 'published', 'author', 'tags', 'id', 'title', 'author_detail', 'summary_detail', 'link', 'wfw_commentrss', 'slash_comments', 'comments', 'published_parsed', 'summary'])), ('http://www.bbc.com/portuguese/topicos/saude/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://feeds.feedburner.com/Exame-Negocios', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title'])), ('http://g1.globo.com/dynamo/musica/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://www.bbc.com/portuguese/topicos/internacional/index.xml', dict_keys(['title_detail', 'updated', 'links', 'guidislink', 'published', 'tags', 'id', 'title', 'summary_detail', 'media_content', 'link', 'img', 'media_thumbnail', 'href', 'updated_parsed', 'dc_identifier', 'published_parsed', 'summary'])), ('http://feeds.folha.uol.com.br/emcimadahora/rss091.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'published_parsed', 'title'])), ('http://g1.globo.com/dynamo/educacao/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://revistagalileu.globo.com/rss/ultimas/feed.xml', dict_keys(['title_detail', 'authors', 'link', 'links', 'guidislink', 'summary_detail', 'id', 'summary', 'author', 'title', 'author_detail'])), ('http://g1.globo.com/dynamo/mundo/rss2.xml', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'summary', 'published', 'tags', 'title', 'published_parsed'])), ('http://feeds.feedburner.com/Exame-GaleriaCiencia', dict_keys(['title_detail', 'link', 'links', 'summary_detail', 'tags', 'summary', 'published', 'published_parsed', 'title', 'feedburner_origlink']))])
>>> a = propriedades.items()
>>> type(a)
<class 'dict_items'>
>>> propriedades.keys()
dict_keys(['http://omelete.com.br.feedsportal.com/cinema', 'http://ig.ultimosegundo.feedsportal.com/c/33511/f/637143/index.rss', 'http://feeds.reuters.com/reuters/businessNews', 'http://www.bbc.com/portuguese/topicos/ciencia_e_tecnologia/index.xml', 'http://feeds.feedburner.com/gizmodobr', 'http://zh.clicrbs.com.br/rs/esportes/ultimas-noticias-rss/', 'http://g1.globo.com/dynamo/brasil/rss2.xml', 'http://www.theverge.com/tech/rss/index.xml', 'http://tecnologia.uol.com.br/ultnot/index.xml', 'http://www.bbc.com/portuguese/index.xml', 'http://feeds.feedburner.com/techtudo', 'http://www.wired.com/category/photo/feed/', 'http://feeds.feedburner.com/Exame-Tecnologia', 'http://www.wired.com/category/business/feed/', 'http://g1.globo.com/dynamo/loterias/rss2.xml', 'http://g1.globo.com/dynamo/tecnologia/rss2.xml', 'http://g1.globo.com/dynamo/concursos-e-emprego/rss2.xml', 'http://zh.clicrbs.com.br/rs/noticias/economia/ultimas-noticias-rss/', 'http://feeds.cnevids.com/brand/wired.mrss', 'http://www.theverge.com/apple/rss/index.xml', 'http://omelete.com.br.feedsportal.com/rss', 'http://feeds.feedburner.com/EXAME-Noticias', 'http://www.bbc.com/portuguese/topicos/cultura/index.xml', 'http://feeds.feedburner.com/EXAME-Marketing', 'http://feeds.feedburner.com/Exame-Economia', 'http://feeds.bbci.co.uk/news/rss.xml', 'http://zh.clicrbs.com.br/rs/ultimas-noticias-rss/', 'http://g1.globo.com/dynamo/rss2.xml', 'http://feeds.feedburner.com/IeeeSpectrum', 'http://www.wired.com/category/design/feed/', 'http://omelete.com.br.feedsportal.com/series-e-tv', 'http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml', 'http://feeds.reuters.com/reuters/technologyNews', 'http://www.wired.com/category/science/science-blogs/feed/', 'http://feeds.reuters.com/news/wealth', 'http://www.bbc.com/portuguese/topicos/brasil/index.xml', 'http://www.theverge.com/google/rss/index.xml', 'http://www.theverge.com/rss/index.xml', 'http://feeds.wired.com/wired/index', 'http://g1.globo.com/dynamo/economia/rss2.xml', 'https://br.noticias.yahoo.com/rss/brasil', 'http://esporte.uol.com.br/ultimas/index.xml', 'http://feeds.feedburner.com/EXAME-Mercados', 'http://feeds.feedburner.com/Exame-Gestao', 'http://rss.uol.com.br/feed/noticias.xml', 'http://feeds.reuters.com/news/artsculture', 'http://www.theverge.com/microsoft/rss/index.xml', 'http://imasters.com.br/feed/', 'http://feeds.reuters.com/reuters/scienceNews', 'http://feeds.reuters.com/reuters/topNews', 'http://www.wired.com/category/science/feed/', 'http://www.bbc.com/portuguese/topicos/economia/index.xml', 'http://rss.uol.com.br/feed/economia.xml', 'http://www.wired.com/category/reviews/feed/', 'http://www.lancenet.com.br/rss/latest/', 'http://feeds.reuters.com/reuters/entertainment', 'http://www.wired.com/category/underwire/feed/', 'http://www.wired.com/category/threatlevel/feed/', 'http://noticias.r7.com/brasil/feed.xml', 'http://omelete.com.br.feedsportal.com/quadrinhos', 'http://feeds.reuters.com/Reuters/worldNews', 'http://omelete.com.br.feedsportal.com/games', 'http://www.wired.com/category/gear/feed/', 'http://www.bbc.com/portuguese/topicos/saude/index.xml', 'http://feeds.feedburner.com/Exame-Negocios', 'http://g1.globo.com/dynamo/musica/rss2.xml', 'http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss', 'http://www.bbc.com/portuguese/topicos/internacional/index.xml', 'http://feeds.folha.uol.com.br/emcimadahora/rss091.xml', 'http://g1.globo.com/dynamo/educacao/rss2.xml', 'http://revistagalileu.globo.com/rss/ultimas/feed.xml', 'http://g1.globo.com/dynamo/mundo/rss2.xml', 'http://feeds.feedburner.com/Exame-GaleriaCiencia'])
>>> for i, j in propriedades.items:
	for m in j:
		if m in em_comum:
			em_comum[m] += 1
		else:
			em_comum[m] = 1

			
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for i, j in propriedades.items:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for i, j in propriedades.items():
	for m in j:
		if m in em_comum:
			em_comum[m] += 1
		else:
			em_comum[m] = 1

			

>>> len(em_comum)
36
>>> em_comum
{'media_keywords': 1, 'authors': 25, 'content_id': 1, 'guidislink': 45, 'media_player': 1, 'figcaption': 1, 'published': 71, 'feedburner_origlink': 12, 'updated': 14, 'id': 45, 'title': 73, 'author_detail': 25, 'summary_detail': 66, 'media_content': 10, 'link': 73, 'wfw_commentrss': 12, 'content': 12, 'media_credit': 1, 'cne_contentid': 1, 'cne_seotitle': 1, 'title_detail': 73, 'href': 10, 'links': 73, 'tags': 51, 'author': 25, 'credit': 1, 'source': 1, 'img': 8, 'media_thumbnail': 10, 'updated_parsed': 14, 'dc_identifier': 7, 'slash_comments': 12, 'comments': 11, 'published_parsed': 71, 'figure': 1, 'summary': 73}
>>> len(propriedades)
73
>>> import operator
>>> sorted_x = sorted(em_comum.items(), key=operator.itemgetter(1))
>>> sorted_x
[('media_keywords', 1), ('content_id', 1), ('media_player', 1), ('figcaption', 1), ('media_credit', 1), ('cne_contentid', 1), ('cne_seotitle', 1), ('credit', 1), ('source', 1), ('figure', 1), ('dc_identifier', 7), ('img', 8), ('media_content', 10), ('href', 10), ('media_thumbnail', 10), ('comments', 11), ('feedburner_origlink', 12), ('wfw_commentrss', 12), ('content', 12), ('slash_comments', 12), ('updated', 14), ('updated_parsed', 14), ('authors', 25), ('author_detail', 25), ('author', 25), ('guidislink', 45), ('id', 45), ('tags', 51), ('summary_detail', 66), ('published', 71), ('published_parsed', 71), ('title', 73), ('link', 73), ('title_detail', 73), ('links', 73), ('summary', 73)]
>>> sorted_x = sorted(em_comum.items(), key=operator.itemgetter(1), reverse=True)
>>> sorted_x
[('title', 73), ('link', 73), ('title_detail', 73), ('links', 73), ('summary', 73), ('published', 71), ('published_parsed', 71), ('summary_detail', 66), ('tags', 51), ('guidislink', 45), ('id', 45), ('authors', 25), ('author_detail', 25), ('author', 25), ('updated', 14), ('updated_parsed', 14), ('feedburner_origlink', 12), ('wfw_commentrss', 12), ('content', 12), ('slash_comments', 12), ('comments', 11), ('media_content', 10), ('href', 10), ('media_thumbnail', 10), ('img', 8), ('dc_identifier', 7), ('media_keywords', 1), ('content_id', 1), ('media_player', 1), ('figcaption', 1), ('media_credit', 1), ('cne_contentid', 1), ('cne_seotitle', 1), ('credit', 1), ('source', 1), ('figure', 1)]
>>> propriedades = {}
>>> erros = []
>>> movidos = []
>>> keyss = {}
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		for j in tmp_parse.entries:
			for m in j.keys():
				keyss[m] = m
		print("Acessado com sucesso: {}".format(i.link_rss))
	elif tmp_parse.status == 301 and len(tmp_parse.entries) > 0:
		for j in tmp_parse.entries:
			for m in j.keys():
				keyss[m] = m
		print("Link: {} - Movido para: {}".format(i.link_rss, tmp_parse.href))
		movidos.append(tmp_parse.href)
	else:
		print("Página {} retornou um erro".format(i.link_rss))
		erros.append(i.link_rss)

		
Página http://www.baixaki.com.br/rss/tecnologia.xml retornou um erro
Acessado com sucesso: http://tecnologia.uol.com.br/ultnot/index.xml
Acessado com sucesso: http://feeds.feedburner.com/IeeeSpectrum
Acessado com sucesso: http://zh.clicrbs.com.br/rs/ultimas-noticias-rss/
Acessado com sucesso: http://zh.clicrbs.com.br/rs/esportes/ultimas-noticias-rss/
Acessado com sucesso: http://zh.clicrbs.com.br/rs/noticias/economia/ultimas-noticias-rss/
Acessado com sucesso: http://rss.uol.com.br/feed/noticias.xml
Acessado com sucesso: http://feeds.folha.uol.com.br/emcimadahora/rss091.xml
Acessado com sucesso: http://ig.ultimosegundo.feedsportal.com/c/33511/f/637143/index.rss
Acessado com sucesso: http://noticias.r7.com/brasil/feed.xml
Acessado com sucesso: https://br.noticias.yahoo.com/rss/brasil
Página http://g1.globo.com/dynamo/rss2.xml retornou um erro
Acessado com sucesso: http://g1.globo.com/dynamo/brasil/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/concursos-e-emprego/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/economia/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/educacao/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/loterias/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/mundo/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/musica/rss2.xml
Acessado com sucesso: http://g1.globo.com/dynamo/tecnologia/rss2.xml
Acessado com sucesso: http://feeds.bbci.co.uk/news/rss.xml
Acessado com sucesso: http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss
Acessado com sucesso: http://imasters.com.br/feed/
Acessado com sucesso: http://feeds.feedburner.com/gizmodobr
Acessado com sucesso: http://www.lancenet.com.br/rss/latest/
Acessado com sucesso: http://feeds.feedburner.com/techtudo
Acessado com sucesso: http://omelete.com.br.feedsportal.com/cinema
Acessado com sucesso: http://omelete.com.br.feedsportal.com/quadrinhos
Acessado com sucesso: http://omelete.com.br.feedsportal.com/series-e-tv
Acessado com sucesso: http://omelete.com.br.feedsportal.com/games
Acessado com sucesso: http://omelete.com.br.feedsportal.com/rss
Acessado com sucesso: http://esporte.uol.com.br/ultimas/index.xml
Acessado com sucesso: http://rss.uol.com.br/feed/economia.xml
Acessado com sucesso: http://feeds.wired.com/wired/index
Acessado com sucesso: http://www.wired.com/category/business/feed/
Acessado com sucesso: http://www.wired.com/category/design/feed/
Acessado com sucesso: http://www.wired.com/category/underwire/feed/
Acessado com sucesso: http://www.wired.com/category/gear/feed/
Acessado com sucesso: http://www.wired.com/category/reviews/feed/
Acessado com sucesso: http://www.wired.com/category/science/feed/
Acessado com sucesso: http://www.wired.com/category/science/science-blogs/feed/
Acessado com sucesso: http://www.wired.com/category/threatlevel/feed/
Acessado com sucesso: http://feeds.cnevids.com/brand/wired.mrss
Acessado com sucesso: http://www.wired.com/category/photo/feed/
Acessado com sucesso: http://www.theverge.com/rss/index.xml
Acessado com sucesso: http://www.theverge.com/tech/rss/index.xml
Acessado com sucesso: http://www.theverge.com/apple/rss/index.xml
Acessado com sucesso: http://www.theverge.com/google/rss/index.xml
Acessado com sucesso: http://www.theverge.com/microsoft/rss/index.xml
Acessado com sucesso: http://feeds.reuters.com/news/artsculture
Acessado com sucesso: http://feeds.reuters.com/reuters/businessNews
Acessado com sucesso: http://feeds.reuters.com/reuters/entertainment
Acessado com sucesso: http://feeds.reuters.com/news/wealth
Acessado com sucesso: http://feeds.reuters.com/reuters/scienceNews
Acessado com sucesso: http://feeds.reuters.com/reuters/technologyNews
Acessado com sucesso: http://feeds.reuters.com/reuters/topNews
Acessado com sucesso: http://feeds.reuters.com/Reuters/worldNews
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Noticias
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Mercados
Acessado com sucesso: http://feeds.feedburner.com/Exame-Negocios
Acessado com sucesso: http://feeds.feedburner.com/Exame-Economia
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Marketing
Acessado com sucesso: http://feeds.feedburner.com/Exame-Tecnologia
Acessado com sucesso: http://feeds.feedburner.com/EXAME-Marketing
Acessado com sucesso: http://feeds.feedburner.com/Exame-Gestao
Acessado com sucesso: http://feeds.feedburner.com/Exame-GaleriaCiencia
Acessado com sucesso: http://revistagalileu.globo.com/rss/ultimas/feed.xml
Acessado com sucesso: http://www.bbc.com/portuguese/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/brasil/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/internacional/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/economia/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/saude/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/ciencia_e_tecnologia/index.xml
Acessado com sucesso: http://www.bbc.com/portuguese/topicos/cultura/index.xml
>>> keys
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    keys
NameError: name 'keys' is not defined
>>> keyss
{'media_keywords': 'media_keywords', 'authors': 'authors', 'content_id': 'content_id', 'guidislink': 'guidislink', 'media_player': 'media_player', 'published': 'published', 'feedburner_origlink': 'feedburner_origlink', 'updated': 'updated', 'id': 'id', 'title': 'title', 'author_detail': 'author_detail', 'summary_detail': 'summary_detail', 'media_content': 'media_content', 'link': 'link', 'wfw_commentrss': 'wfw_commentrss', 'dc_identifier': 'dc_identifier', 'media_credit': 'media_credit', 'media_text': 'media_text', 'cne_contentid': 'cne_contentid', 'figcaption': 'figcaption', 'cne_seotitle': 'cne_seotitle', 'title_detail': 'title_detail', 'href': 'href', 'links': 'links', 'cne_season': 'cne_season', 'tags': 'tags', 'author': 'author', 'credit': 'credit', 'cne_series': 'cne_series', 'source': 'source', 'img': 'img', 'media_thumbnail': 'media_thumbnail', 'updated_parsed': 'updated_parsed', 'content': 'content', 'slash_comments': 'slash_comments', 'comments': 'comments', 'published_parsed': 'published_parsed', 'figure': 'figure', 'summary': 'summary'}
>>> len(keyss)
39
>>> len(sorted_x)
36
>>> tmp_k = []
>>> for i in sorted_x:
	tmp_k.append(i[0])

	
>>> tmp_k
['title', 'link', 'title_detail', 'links', 'summary', 'published', 'published_parsed', 'summary_detail', 'tags', 'guidislink', 'id', 'authors', 'author_detail', 'author', 'updated', 'updated_parsed', 'feedburner_origlink', 'wfw_commentrss', 'content', 'slash_comments', 'comments', 'media_content', 'href', 'media_thumbnail', 'img', 'dc_identifier', 'media_keywords', 'content_id', 'media_player', 'figcaption', 'media_credit', 'cne_contentid', 'cne_seotitle', 'credit', 'source', 'figure']
>>> len(tmp_k)
36
>>> len(sorted_k)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    len(sorted_k)
NameError: name 'sorted_k' is not defined
>>> len(sorted_x)
36
>>> a = keyss.values()
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a[0]
TypeError: 'dict_values' object does not support indexing
>>> dir(a)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> a
dict_values(['media_keywords', 'authors', 'content_id', 'guidislink', 'media_player', 'published', 'feedburner_origlink', 'updated', 'id', 'title', 'author_detail', 'summary_detail', 'media_content', 'link', 'wfw_commentrss', 'dc_identifier', 'media_credit', 'media_text', 'cne_contentid', 'figcaption', 'cne_seotitle', 'title_detail', 'href', 'links', 'cne_season', 'tags', 'author', 'credit', 'cne_series', 'source', 'img', 'media_thumbnail', 'updated_parsed', 'content', 'slash_comments', 'comments', 'published_parsed', 'figure', 'summary'])
>>> for i in a:
	print i
	
SyntaxError: Missing parentheses in call to 'print'
>>> for i in a:
	print(i)

	
media_keywords
authors
content_id
guidislink
media_player
published
feedburner_origlink
updated
id
title
author_detail
summary_detail
media_content
link
wfw_commentrss
dc_identifier
media_credit
media_text
cne_contentid
figcaption
cne_seotitle
title_detail
href
links
cne_season
tags
author
credit
cne_series
source
img
media_thumbnail
updated_parsed
content
slash_comments
comments
published_parsed
figure
summary
>>> for i in a:
	if i not in sorted_x:
		print(i)

		
media_keywords
authors
content_id
guidislink
media_player
published
feedburner_origlink
updated
id
title
author_detail
summary_detail
media_content
link
wfw_commentrss
dc_identifier
media_credit
media_text
cne_contentid
figcaption
cne_seotitle
title_detail
href
links
cne_season
tags
author
credit
cne_series
source
img
media_thumbnail
updated_parsed
content
slash_comments
comments
published_parsed
figure
summary
>>> "summary" in sorted_x
False
>>> sorted_x
[('title', 73), ('link', 73), ('title_detail', 73), ('links', 73), ('summary', 73), ('published', 71), ('published_parsed', 71), ('summary_detail', 66), ('tags', 51), ('guidislink', 45), ('id', 45), ('authors', 25), ('author_detail', 25), ('author', 25), ('updated', 14), ('updated_parsed', 14), ('feedburner_origlink', 12), ('wfw_commentrss', 12), ('content', 12), ('slash_comments', 12), ('comments', 11), ('media_content', 10), ('href', 10), ('media_thumbnail', 10), ('img', 8), ('dc_identifier', 7), ('media_keywords', 1), ('content_id', 1), ('media_player', 1), ('figcaption', 1), ('media_credit', 1), ('cne_contentid', 1), ('cne_seotitle', 1), ('credit', 1), ('source', 1), ('figure', 1)]
>>> for i in a:
	if i not in tmp_k:
		print(i)

		
media_text
cne_season
cne_series
>>> from lxml.html.clean import Cleaner
>>> a = fp.parse("http://www.theverge.com/rss/index.xml")
>>> teste = a.entries[0]
>>> teste.keys()
dict_keys(['title_detail', 'authors', 'updated', 'links', 'guidislink', 'id', 'author', 'summary', 'published', 'title', 'author_detail', 'link', 'updated_parsed', 'content', 'published_parsed'])
>>> cleaner = Cleaner(remove_unknown_tags=False, remove_tags=['br', 'a', 'img'])
>>> cleaner.clean_html(teste.summary)
"<div>\n\n\n\n  \t\t <p>Worldwide. Always On. One hundred countries. Listen to Beats 1 for more than a few songs and without fail someone will get on a mic to remind you the global reach of Apple Music's tentpole radio station. But while the ambition is there, does Beats 1 translate globally? Turns out, <em>The Verge</em> is also worldwide and always on. So we tasked some of our writers both in the US and internationally — specifically London, Tokyo, and Paris —\xa0to listen to the first 24 hours of Beats 1 radio. This is a running log. </p>\n  <p>\n    Continue reading…\n  </p></div>"
>>> teste.summary
'<img alt="" src="https://cdn0.vox-cdn.com/thumbor/oAAoWTq1SGMSGYSNNlUP9Sl7ZjY=/352x0:1101x499/800x536/cdn0.vox-cdn.com/uploads/chorus_image/image/46663636/1500x500.0.0.png" />\n\n\n\n  \t\t <p>Worldwide. Always On. One hundred countries. Listen to Beats 1 for more than a few songs and without fail someone will get on a mic to remind you the global reach of Apple Music\'s tentpole radio station. But while the ambition is there, does Beats 1 translate globally? Turns out, <em>The Verge</em> is also worldwide and always on. So we tasked some of our writers both in the US and internationally — specifically London, Tokyo, and Paris —\xa0to listen to the first 24 hours of Beats 1 radio. This is a running log. </p>\n  <p>\n    <a href="http://www.theverge.com/2015/7/2/8883215/beats-1-radio-apple-music-zane-lowe-first-24">Continue reading&hellip;</a>\n  </p>'
>>> cleaner = Cleaner(remove_unknown_tags=False, remove_tags=['br', 'a', 'img', 'div'])
>>> cleaner.clean_html(teste.summary)
"<div>\n\n\n\n  \t\t <p>Worldwide. Always On. One hundred countries. Listen to Beats 1 for more than a few songs and without fail someone will get on a mic to remind you the global reach of Apple Music's tentpole radio station. But while the ambition is there, does Beats 1 translate globally? Turns out, <em>The Verge</em> is also worldwide and always on. So we tasked some of our writers both in the US and internationally — specifically London, Tokyo, and Paris —\xa0to listen to the first 24 hours of Beats 1 radio. This is a running log. </p>\n  <p>\n    Continue reading…\n  </p></div>"
>>> del(cleaner)
>>> cleaner = Cleaner(remove_unknown_tags=False, remove_tags=['br', 'a', 'img', 'div'])
>>> cleaner.clean_html(teste.summary)
"<div>\n\n\n\n  \t\t <p>Worldwide. Always On. One hundred countries. Listen to Beats 1 for more than a few songs and without fail someone will get on a mic to remind you the global reach of Apple Music's tentpole radio station. But while the ambition is there, does Beats 1 translate globally? Turns out, <em>The Verge</em> is also worldwide and always on. So we tasked some of our writers both in the US and internationally — specifically London, Tokyo, and Paris —\xa0to listen to the first 24 hours of Beats 1 radio. This is a running log. </p>\n  <p>\n    Continue reading…\n  </p></div>"
>>> cleaner = Cleaner(remove_unknown_tags=False, remove_tags=['br', 'a', 'img', 'div', 'p'])
>>> cleaner.clean_html(teste.summary)
"<div>\n\n\n\n  \t\t Worldwide. Always On. One hundred countries. Listen to Beats 1 for more than a few songs and without fail someone will get on a mic to remind you the global reach of Apple Music's tentpole radio station. But while the ambition is there, does Beats 1 translate globally? Turns out, <em>The Verge</em> is also worldwide and always on. So we tasked some of our writers both in the US and internationally — specifically London, Tokyo, and Paris —\xa0to listen to the first 24 hours of Beats 1 radio. This is a running log. \n  \n    Continue reading…\n  </div>"
>>> cleaner = Cleaner(remove_unknown_tags=False, remove_tags=['br', 'a', 'img', 'div', 'p'])
>>> from lxml.html.clean import clean_html
>>> tree = clean_html(teste.summary)
>>> text = tree.getroot().text_content()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    text = tree.getroot().text_content()
AttributeError: 'str' object has no attribute 'getroot'
>>> cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
>>> cleaner.clean_html(teste.summary)
"<div>\n\n\n\n  \t\t Worldwide. Always On. One hundred countries. Listen to Beats 1 for more than a few songs and without fail someone will get on a mic to remind you the global reach of Apple Music's tentpole radio station. But while the ambition is there, does Beats 1 translate globally? Turns out, The Verge is also worldwide and always on. So we tasked some of our writers both in the US and internationally — specifically London, Tokyo, and Paris —\xa0to listen to the first 24 hours of Beats 1 radio. This is a running log. \n  \n    Continue reading…\n  </div>"
>>> 
