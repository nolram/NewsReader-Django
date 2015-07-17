Python 3.4.2 (default, Jan 12 2015, 12:13:20) 
[GCC 4.9.2 20150107 (Red Hat 4.9.2-5)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from Crawler.add_some_sites import PrimeiraAdicao
>>> a = PrimeiraAdicao()
>>> a.add_pages()
Adicionando os sites...
Adicionando os links RSS
Término do algoritmo...
>>> import feedparser as fp
>>> from Crawler.models import LinksRSS
>>> all = LinksRSS.objects.all()
>>> all_links = LinksRSS.objects.all()
>>> del all
>>> all
<built-in function all>
>>> propriedades = {}
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.code == 200 and tmp_parse.bozo == 0:
		propriedades[i.fk_sites.titulo] = tmp_parse.entries[0].keys()

		
Traceback (most recent call last):
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 399, in __getattr__
    return self.__getitem__(key)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 357, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'code'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 3, in <module>
    if tmp_parse.code == 200 and tmp_parse.bozo == 0:
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 401, in __getattr__
    raise AttributeError("object has no attribute '%s'" % key)
AttributeError: object has no attribute 'code'
>>> tmp_parse.status_code
Traceback (most recent call last):
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 399, in __getattr__
    return self.__getitem__(key)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 357, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'status_code'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tmp_parse.status_code
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 401, in __getattr__
    raise AttributeError("object has no attribute '%s'" % key)
AttributeError: object has no attribute 'status_code'
>>> tmp_parse.keys()
dict_keys(['headers', 'href', 'encoding', 'version', 'bozo_exception', 'status', 'entries', 'bozo', 'namespaces', 'feed'])
>>> tmp_parse.status
403
>>> tmp_parse.bozo
1
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and tmp_parse.bozo == 0:
		propriedades[i.fk_sites.titulo] = tmp_parse.entries[0].keys()
	else:
		print("Página {} retornou um erro".format(i.link_rss))

		
Página http://www.baixaki.com.br/rss/tecnologia.xml retornou um erro
Página http://g1.globo.com/dynamo/rss2.xml retornou um erro
Página http://feeds.bbci.co.uk/news/rss.xml retornou um erro
Página http://imasters.com.br/feed/ retornou um erro
Página http://rss.esporte.uol.com.br/ultimas/index.xml retornou um erro
Página http://rss.noticias.uol.com.br/economia/ultnot/index.xml retornou um erro
Página http://www.theverge.com/tech/rss/index.xml retornou um erro
Página http://revistagalileu.globo.com/rss/ultimas/feed.xml retornou um erro
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    tmp_parse = fp.parse(i.link_rss)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 3841, in parse
    f = _open_resource(url_file_stream_or_string, etag, modified, agent, referrer, handlers, request_headers)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 2866, in _open_resource
    return opener.open(request)
  File "/usr/lib64/python3.4/urllib/request.py", line 461, in open
    response = meth(req, response)
  File "/usr/lib64/python3.4/urllib/request.py", line 571, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib64/python3.4/urllib/request.py", line 493, in error
    result = self._call_chain(*args)
  File "/usr/lib64/python3.4/urllib/request.py", line 433, in _call_chain
    result = func(*args)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 2766, in http_error_301
    code, msg, hdrs)
  File "/usr/lib64/python3.4/urllib/request.py", line 676, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/usr/lib64/python3.4/urllib/request.py", line 455, in open
    response = self._open(req, data)
  File "/usr/lib64/python3.4/urllib/request.py", line 473, in _open
    '_open', req)
  File "/usr/lib64/python3.4/urllib/request.py", line 433, in _call_chain
    result = func(*args)
  File "/usr/lib64/python3.4/urllib/request.py", line 1202, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "/usr/lib64/python3.4/urllib/request.py", line 1177, in do_open
    r = h.getresponse()
  File "/usr/lib64/python3.4/http/client.py", line 1172, in getresponse
    response.begin()
  File "/usr/lib64/python3.4/http/client.py", line 351, in begin
    version, status, reason = self._read_status()
  File "/usr/lib64/python3.4/http/client.py", line 313, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/usr/lib64/python3.4/socket.py", line 371, in readinto
    return self._sock.recv_into(b)
KeyboardInterrupt
>>> propriedades = {}
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and tmp_parse.bozo == 0:
		propriedades[i.fk_sites.titulo] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
	else:
		print("Página {} retornou um erro".format(i.link_rss))

		
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
Página http://feeds.bbci.co.uk/news/rss.xml retornou um erro
Acessado com sucesso: http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss
Página http://imasters.com.br/feed/ retornou um erro
Acessado com sucesso: http://feeds.feedburner.com/gizmodobr
Acessado com sucesso: http://www.lancenet.com.br/rss/latest/
Acessado com sucesso: http://feeds.feedburner.com/techtudo
Acessado com sucesso: http://omelete.com.br.feedsportal.com/cinema
Acessado com sucesso: http://omelete.com.br.feedsportal.com/quadrinhos
Acessado com sucesso: http://omelete.com.br.feedsportal.com/series-e-tv
Acessado com sucesso: http://omelete.com.br.feedsportal.com/games
Acessado com sucesso: http://omelete.com.br.feedsportal.com/rss
Página http://rss.esporte.uol.com.br/ultimas/index.xml retornou um erro
Página http://rss.noticias.uol.com.br/economia/ultnot/index.xml retornou um erro
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
Página http://www.theverge.com/apple/rss/index.xml retornou um erro
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
Página http://revistagalileu.globo.com/rss/ultimas/feed.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/economia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/saude/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/cultura/ retornou um erro
>>> len(propriedades)
17
>>> a = fp.parse("http://www.bbc.com/portuguese/index.xml")
>>> a.bozo
0
>>> a.status
200
>>> erros = []
>>> propriedades = {}
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and tmp_parse.bozo == 0:
		propriedades[i.fk_sites.titulo] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
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
Página http://feeds.bbci.co.uk/news/rss.xml retornou um erro
Acessado com sucesso: http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss
Página http://imasters.com.br/feed/ retornou um erro
Acessado com sucesso: http://feeds.feedburner.com/gizmodobr
Acessado com sucesso: http://www.lancenet.com.br/rss/latest/
Acessado com sucesso: http://feeds.feedburner.com/techtudo
Acessado com sucesso: http://omelete.com.br.feedsportal.com/cinema
Acessado com sucesso: http://omelete.com.br.feedsportal.com/quadrinhos
Acessado com sucesso: http://omelete.com.br.feedsportal.com/series-e-tv
Acessado com sucesso: http://omelete.com.br.feedsportal.com/games
Acessado com sucesso: http://omelete.com.br.feedsportal.com/rss
Página http://rss.esporte.uol.com.br/ultimas/index.xml retornou um erro
Página http://rss.noticias.uol.com.br/economia/ultnot/index.xml retornou um erro
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
Página http://www.theverge.com/apple/rss/index.xml retornou um erro
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
Página http://revistagalileu.globo.com/rss/ultimas/feed.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/economia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/saude/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/cultura/ retornou um erro
>>> erros
['http://www.baixaki.com.br/rss/tecnologia.xml', 'http://feeds.bbci.co.uk/news/rss.xml', 'http://imasters.com.br/feed/', 'http://rss.esporte.uol.com.br/ultimas/index.xml', 'http://rss.noticias.uol.com.br/economia/ultnot/index.xml', 'http://www.theverge.com/apple/rss/index.xml', 'http://revistagalileu.globo.com/rss/ultimas/feed.xml', 'http://www.bbc.co.uk/portuguese/index.xml', 'http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml', 'http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml', 'http://www.bbc.co.uk/portuguese/topicos/economia/', 'http://www.bbc.co.uk/portuguese/topicos/saude/', 'http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/', 'http://www.bbc.co.uk/portuguese/topicos/cultura/']
>>> a = fp.parse("http://feeds.bbci.co.uk/news/rss.xml")
>>> a.status
200
>>> a.bozo
1
>>> a.keys()
dict_keys(['headers', 'href', 'encoding', 'status', 'entries', 'namespaces', 'feed', 'version', 'updated_parsed', 'bozo_exception', 'updated', 'bozo'])
>>> a.bozo_exception
CharacterEncodingOverride('document declared as us-ascii, but parsed as utf-8',)
>>> from Scripts.threading import Future
>>> def em_comum():
	propriedades = {}
	erros = []
	for i in all_links:
		tmp_parse = fp.parse(i.link_rss)
		if tmp_parse.status == 200 and tmp_parse.bozo == 0:
			propriedades[i.fk_sites.titulo] = tmp_parse.entries[0].keys()
			print("Acessado com sucesso: {}".format(i.link_rss))
		else:
			print("Página {} retornou um erro".format(i.link_rss))
		erros.append(i.link_rss)

		
>>> a = Future(em_comum)
Página http://www.baixaki.com.br/rss/tecnologia.xml retornou um erro
>>> 
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
Página http://feeds.bbci.co.uk/news/rss.xml retornou um erro
Acessado com sucesso: http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss
Página http://imasters.com.br/feed/ retornou um erro
Acessado com sucesso: http://feeds.feedburner.com/gizmodobr
Acessado com sucesso: http://www.lancenet.com.br/rss/latest/
Acessado com sucesso: http://feeds.feedburner.com/techtudo
Acessado com sucesso: http://omelete.com.br.feedsportal.com/cinema
Acessado com sucesso: http://omelete.com.br.feedsportal.com/quadrinhos
Acessado com sucesso: http://omelete.com.br.feedsportal.com/series-e-tv
Acessado com sucesso: http://omelete.com.br.feedsportal.com/games
Acessado com sucesso: http://omelete.com.br.feedsportal.com/rss
Página http://rss.esporte.uol.com.br/ultimas/index.xml retornou um erro
Página http://rss.noticias.uol.com.br/economia/ultnot/index.xml retornou um erro
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
Página http://revistagalileu.globo.com/rss/ultimas/feed.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/economia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/saude/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/cultura/ retornou um erro
s
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a.print()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.print()
AttributeError: 'Future' object has no attribute 'print'
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(a)
TypeError: Can't convert 'NoneType' object to str implicitly
>>> len(erros)
14
>>> a = fp.parse("http://revistagalileu.globo.com/rss/ultimas/feed.xml")
>>> a.status
200
>>> a.bozo
1
>>> a.bozo_exception
CharacterEncodingOverride('document declared as us-ascii, but parsed as utf-8',)
>>> b = a.entries
>>> len(b)
25
>>> len(propriedades)
17
>>> len(erros)
14
>>> propriedades = {}
>>> erros = []
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		propriedades[i.link_rss] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
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
Página http://globoesporte.globo.com/servico/semantica/editorias/plantao/feed.rss retornou um erro
Acessado com sucesso: http://imasters.com.br/feed/
Acessado com sucesso: http://feeds.feedburner.com/gizmodobr
Acessado com sucesso: http://www.lancenet.com.br/rss/latest/
Acessado com sucesso: http://feeds.feedburner.com/techtudo
Acessado com sucesso: http://omelete.com.br.feedsportal.com/cinema
Acessado com sucesso: http://omelete.com.br.feedsportal.com/quadrinhos
Acessado com sucesso: http://omelete.com.br.feedsportal.com/series-e-tv
Acessado com sucesso: http://omelete.com.br.feedsportal.com/games
Acessado com sucesso: http://omelete.com.br.feedsportal.com/rss
Página http://rss.esporte.uol.com.br/ultimas/index.xml retornou um erro
Página http://rss.noticias.uol.com.br/economia/ultnot/index.xml retornou um erro
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
Página http://www.bbc.co.uk/portuguese/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/economia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/saude/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/cultura/ retornou um erro
>>> len(erros)
12
>>> a = fp.parse("http://rss.esporte.uol.com.br/ultimas/index.xml")
>>> a.bozo_exception
Traceback (most recent call last):
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 399, in __getattr__
    return self.__getitem__(key)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 357, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'bozo_exception'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.bozo_exception
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 401, in __getattr__
    raise AttributeError("object has no attribute '%s'" % key)
AttributeError: object has no attribute 'bozo_exception'
>>> a.keys()
dict_keys(['headers', 'href', 'encoding', 'status', 'entries', 'namespaces', 'feed', 'version', 'updated_parsed', 'etag', 'updated', 'bozo'])
>>> a.bozo
0
>>> len(a.entries)
20
>>> a.status
301
>>> a.href
'http://esporte.uol.com.br/ultimas/index.xml'
>>> propriedades = {}
>>> erros = []
>>> movidos = []
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		propriedades[i.link_rss] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
	elif tmp_parse.status == 301:
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
Link: http://rss.esporte.uol.com.br/ultimas/index.xml - Movido para: http://esporte.uol.com.br/ultimas/index.xml
Link: http://rss.noticias.uol.com.br/economia/ultnot/index.xml - Movido para: http://rss.uol.com.br/feed/economia.xml
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
Link: http://www.bbc.co.uk/portuguese/index.xml - Movido para: http://www.bbc.com/portuguese/index.xml
Link: http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml - Movido para: http://www.bbc.com/portuguese/topicos/brasil/index.xml
Link: http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml - Movido para: http://www.bbc.com/portuguese/topicos/internacional/index.xml
Link: http://www.bbc.co.uk/portuguese/topicos/economia/ - Movido para: http://www.bbc.com/portuguese/topicos/economia
Link: http://www.bbc.co.uk/portuguese/topicos/saude/ - Movido para: http://www.bbc.com/portuguese/topicos/saude
Link: http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/ - Movido para: http://www.bbc.com/portuguese/topicos/ciencia_e_tecnologia
Link: http://www.bbc.co.uk/portuguese/topicos/cultura/ - Movido para: http://www.bbc.com/portuguese/topicos/cultura
>>> len(erros)
1
>>> movidos = []
>>> erros = []
>>> propriedades = {}
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		propriedades[i.link_rss] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
	elif tmp_parse.status == 301 and len(tmp_parse.entries) > 0:
		propriedades[i.href] = tmp_parse.entries[0].keys()
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
Traceback (most recent call last):
  File "<pyshell#80>", line 7, in <module>
    propriedades[i.href] = tmp_parse.entries[0].keys()
AttributeError: 'LinksRSS' object has no attribute 'href'
>>> movidos = []
>>> erros = []
>>> propriedades = {}
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
Link: http://rss.esporte.uol.com.br/ultimas/index.xml - Movido para: http://esporte.uol.com.br/ultimas/index.xml
Link: http://rss.noticias.uol.com.br/economia/ultnot/index.xml - Movido para: http://rss.uol.com.br/feed/economia.xml
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
Link: http://www.bbc.co.uk/portuguese/index.xml - Movido para: http://www.bbc.com/portuguese/index.xml
Link: http://www.bbc.co.uk/portuguese/topicos/brasil/index.xml - Movido para: http://www.bbc.com/portuguese/topicos/brasil/index.xml
Link: http://www.bbc.co.uk/portuguese/topicos/internacional/index.xml - Movido para: http://www.bbc.com/portuguese/topicos/internacional/index.xml
Página http://www.bbc.co.uk/portuguese/topicos/economia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/saude/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/ciencia_e_tecnologia/ retornou um erro
Página http://www.bbc.co.uk/portuguese/topicos/cultura/ retornou um erro
>>> len(erros)
5
>>> 
movidos = []
>>> erros = []
>>> propriedades = {}
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
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 399, in __getattr__
    return self.__getitem__(key)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 357, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'status'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#91>", line 3, in <module>
    if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 401, in __getattr__
    raise AttributeError("object has no attribute '%s'" % key)
AttributeError: object has no attribute 'status'

>>> movidos = []
>>> erros = []
>>> propriedades = {}
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
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 399, in __getattr__
    return self.__getitem__(key)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 357, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'status'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#96>", line 3, in <module>
    if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 401, in __getattr__
    raise AttributeError("object has no attribute '%s'" % key)
AttributeError: object has no attribute 'status'
>>> tmp_parse
{'entries': [], 'bozo': 1, 'bozo_exception': URLError(gaierror(-5, 'No address associated with hostname'),), 'feed': {}}
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
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 399, in __getattr__
    return self.__getitem__(key)
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 357, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'status'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#99>", line 3, in <module>
    if tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/feedparser.py", line 401, in __getattr__
    raise AttributeError("object has no attribute '%s'" % key)
AttributeError: object has no attribute 'status'
>>> for i in all_links:
	tmp_parse = fp.parse(i.link_rss)
	if tmp_parse.bozo == 1 and tmp_parse.status == 200 and len(tmp_parse.entries) > 0:
		propriedades[i.link_rss] = tmp_parse.entries[0].keys()
		print("Acessado com sucesso: {}".format(i.link_rss))
	elif tmp_parse.status == 301 and len(tmp_parse.entries) > 0:
		propriedades[tmp_parse.href] = tmp_parse.entries[0].keys()
		print("Link: {} - Movido para: {}".format(i.link_rss, tmp_parse.href))
		movidos.append(tmp_parse.href)
	else:
		print("Página {} retornou um erro".format(i.link_rss))
		erros.append(i.link_rss)
