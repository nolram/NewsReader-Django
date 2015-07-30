Python 3.4.2 (default, Jul  9 2015, 17:24:30) 
[GCC 5.1.1 20150618 (Red Hat 5.1.1-4)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from Crawler.models import Postagens
>>> postagens = Postagens.objects.all()
>>> textos = {}
>>> for post in postagens:
	if len(post.texto) > 0:
		textos[post.pk] = post.texto
	else:
		textos[post.pk] = post.titulo

		
>>> len(textos)
2811
>>> textos.values()[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    textos.values()[0]
TypeError: 'dict_values' object does not support indexing
>>> textos.items[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    textos.items[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> textos.items()[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    textos.items()[0]
TypeError: 'dict_items' object does not support indexing
>>> todos_o_texto = ""
>>> for i,j in textos.items():
	todos_o_texto += j

	
>>> len(todos_o_texto)
1338942
>>> todos_os_textos = ""
>>> todos_os_textos = []
>>> todos_o_texto = ""
>>> for i,j in textos.items():
	todos_os_textos.append(j)

	
>>> 
>>> stop_words = nltk.corpus.stopwords.words('portuguese')
>>> palavras = []
>>> for def normalizar_palavras(self, texto):
        regex = re.compile('[{0}]'.format(re.escape(string.punctuation)))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        palavras = []
        linha = texto.replace("\n", " ")
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
SyntaxError: invalid syntax
>>> def normalizar_palavras(self, texto):
        regex = re.compile('[{0}]'.format(re.escape(string.punctuation)))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        palavras = []
        linha = texto.replace("\n", " ")
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

>>> import re
>>> import html
>>> textos = {}
>>> for post in postagens:
	if len(post.texto) > 0:
		textos[post.pk] = nltk.clean_html(html.unescape(post.texto))
	else:
		textos[post.pk] = nltk.clean_html(html.unescape(post.titulo))

		
Traceback (most recent call last):
  File "<pyshell#34>", line 3, in <module>
    textos[post.pk] = nltk.clean_html(html.unescape(post.texto))
  File "/home/nolram/Virtualenv/py3_django/lib/python3.4/site-packages/nltk/util.py", line 346, in clean_html
    raise NotImplementedError ("To remove HTML markup, use BeautifulSoup's get_text() function")
NotImplementedError: To remove HTML markup, use BeautifulSoup's get_text() function
>>> from lxml.html.clean import Cleaner
>>> cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
>>> for post in postagens:
	if len(post.texto) > 0:
		textos[post.pk] = cleaner.clean_html(html.unescape(post.texto))
	else:
		textos[post.pk] = cleaner.clean_html(html.unescape(post.titulo))

		
>>> textos = {}
>>> for post in postagens:
	if len(post.texto) > 0:
		textos[post.pk] = cleaner.clean_html(html.unescape(post.texto))
	else:
		textos[post.pk] = cleaner.clean_html(html.unescape(post.titulo))

		
>>> palavras = []
>>> for i, j in textos.items():
	palavras.extend(normalizar_palavras(j))

	
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    palavras.extend(normalizar_palavras(j))
TypeError: normalizar_palavras() missing 1 required positional argument: 'texto'
>>> def normalizar_palavras(texto):
        regex = re.compile('[{0}]'.format(re.escape(string.punctuation)))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        palavras = []
        linha = texto.replace("\n", " ")
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

>>> for i, j in textos.items():
	palavras.extend(normalizar_palavras(j))

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    palavras.extend(normalizar_palavras(j))
  File "<pyshell#47>", line 2, in normalizar_palavras
    regex = re.compile('[{0}]'.format(re.escape(string.punctuation)))
NameError: name 'string' is not defined
>>> import string
>>> for i, j in textos.items():
	palavras.extend(normalizar_palavras(j))

	
>>> len(palavras)
133361
>>> palavras[0]
'div'
>>> palavras[1]
'surfista'
>>> palavras[2]
'australiano'
>>> palavras[3]
'mick'
>>> palavras[4]
'fanning'
>>> fd = nltk.FreqDist(palavras)
>>> fd[0]
0
>>> fd[1]
0
>>> fd[:50]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    fd[:50]
TypeError: unhashable type: 'slice'
>>> fd.samples()[:50]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    fd.samples()[:50]
AttributeError: 'FreqDist' object has no attribute 'samples'
>>> dir(fd)
['B', 'N', 'Nr', '__add__', '__and__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__le__', '__len__', '__lt__', '__missing__', '__module__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__unicode__', '__weakref__', '_cumulative_frequencies', '_keep_positive', 'clear', 'copy', 'elements', 'freq', 'fromkeys', 'get', 'hapaxes', 'items', 'keys', 'max', 'most_common', 'pformat', 'plot', 'pop', 'popitem', 'pprint', 'r_Nr', 'setdefault', 'subtract', 'tabulate', 'unicode_repr', 'update', 'values']
>>> fd
FreqDist({'é': 1381, 'the': 1152, 'div': 722, 'to': 531, 'of': 506, 'on': 411, 'sobre': 407, 'in': 401, 'anos': 388, 'ser': 385, ...})
>>> stop_words
['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']
>>> type(stop_words)
<class 'list'>
>>> "é" in stop_words
False
>>> "as" in stop_words
True
>>> def normalizar_palavras(texto):
        regex = re.compile('[{0}]'.format(re.escape(string.punctuation)))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        stop_words.extend(nltk.corpus.stopwords.words('english'))
        palavras = []
        linha = texto.replace("\n", " ")
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

>>> palavras = []
>>> for i, j in textos.items():
	palavras.extend(normalizar_palavras(j))

	
>>> stop_words
['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']
>>> stop_words.extend(nltk.corpus.stopwords.words('english'))
>>> stop_words
['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
>>> 
fd = nltk.FreqDist(palavras)
>>> fd
FreqDist({'é': 1381, 'div': 722, 'sobre': 407, 'anos': 388, 'ser': 385, 'nesta': 368, '—': 336, 'federal': 314, 'ainda': 311, 'governo': 290, ...})
>>> string.pun
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    string.pun
AttributeError: 'module' object has no attribute 'pun'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> "—" == "-"
False
>>> '[{0}]'.format(re.escape(string.punctuation))
'[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
>>> '[{0}{1}]'.format(re.escape(string.punctuation),'—')
'[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~—]'
>>> '[{0}{1}]'.format(re.escape(string.punctuation),re.escape('—'))
'[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~\\—]'
>>> def normalizar_palavras(texto):
        regex = re.compile('[{0}{1}]'.format(re.escape(string.punctuation),re.escape('—')))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        stop_words.extend(nltk.corpus.stopwords.words('english'))
        palavras = []
        linha = texto.replace("\n", " ")
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

>>> def normalizar_palavras(texto):
        regex = re.compile('[{0}{1}]'.format(re.escape(string.punctuation),re.escape('—')))
        stop_words = nltk.corpus.stopwords.words('portuguese')
        stop_words.extend(nltk.corpus.stopwords.words('english'))
        stop_words.extend(["é", "div"])
        palavras = []
        linha = texto.replace("\n", " ")
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

>>> palavras = []
>>> for i, j in textos.items():
	palavras.extend(normalizar_palavras(j))

	
>>> fd = nltk.FreqDist(palavras)
>>> fd
FreqDist({'sobre': 407, 'anos': 390, 'ser': 385, 'nesta': 368, 'federal': 314, 'ainda': 311, 'governo': 290, 'segundafeira': 283, 'brasil': 271, 'presidente': 253, ...})
>>> nomes = nltk.corpus.names
>>> type(nomes)
<class 'nltk.corpus.util.LazyCorpusLoader'>
>>> nomes = nltk.corpus.names()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    nomes = nltk.corpus.names()
TypeError: 'WordListCorpusReader' object is not callable
>>> nomes = nltk.corpus.names
>>> nomes = nltk.corpus.names.words("male.txt")
>>> type(nomes)
<class 'list'>
>>> "marlon" in nomes
False
>>> "Marlon" in nomes
True
>>> len(nomes)
2943
>>> from nltk.corpus import names
>>> labeled_names = ([(name, "male") for name in names.words('male.txt')] + [(name, "female") for name in names.words('female.txt')])
>>> import random
>>> random.shuffle(labeled_names)
>>> featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
  File "<pyshell#108>", line 1, in <listcomp>
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
NameError: name 'gender_features' is not defined
>>> 
