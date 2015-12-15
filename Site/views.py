# -.- encoding:utf-8 -.-
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import Http404

#from haystack.query import SearchQuerySet

from Crawler.models import Postagens, Categorias, Tags, TagsPostagens
from Site.forms import PesquisaForms
from Site.models import ProvidersUser, ProvedoresDeLogin, TokenLogin


def index(request):
    if request.user.is_authenticated():
        return render(request, "site/index_logado.html", {"usuario": request.user})
    else:
        return render(request, "index.html")


def pag_login(request):
    erros = {}
    if request.method == "POST":
        username = request.POST.get("inputEmail")
        password = request.POST.get("inputPassword")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                erros["erro"] = "O seu login está desativado, entre em contato com o administrador"
        else:
            erros["erro"] = "O seu login e/ou sua senha estão incorretos"

    return render(request, "login.html", erros)


@login_required
def pag_postagem(request, id_postagem):
    try:
        postagem = Postagens.objects.get(id_postagem=id_postagem)
    except Postagens.DoesNotExist:
        raise Http404("Nenhuma postagem encontrada com esse ID.")

    dic_pos = {"postagem": postagem, "usuario": request.user}
    return render(request, "site/postagem.html", dic_pos)


def logout_view(request):
    logout(request)
    return redirect("/")

# def pesquisa_pagina(request):
#     if request.method == "GET":
#         form = PesquisaForms(request.GET)
#         if form.is_valid():
#             q = form.cleaned_data["query"]
#             pagina = form.cleaned_data["page"]
#
#             if q[0] == "#":
#                 pesquisa = TagsPostagens.objects.select_related("fk_tag").filter(fk_tag__tag=q[1:].lower())\
#                     .select_related("fk_postagem")
#                 paginator = Paginator(pesquisa, 20)
#                 tag = True
#             else:
#                 pesquisa = SearchQuerySet().filter(content=q).order_by('-horario_postagem_site')
#                 paginator = Paginator(pesquisa, 20)
#                 tag = False
#
#             try:
#                 postagens = paginator.page(pagina)
#             except PageNotAnInteger:
#                 postagens = paginator.page(1)
#             except EmptyPage:
#                 postagens = paginator.page(paginator.num_pages)
#
#             context = {
#                 "tag": tag,
#                 "page": postagens,
#                 "paginator": paginator,
#                 "query": q
#             }
#         else:
#             context = {
#                 "erro": "Query Inválida!!!"
#             }
#
#         return render_to_response("site/search.html", context, context_instance=RequestContext(request))


@csrf_exempt
def get_last_news(request, pagina):
    categoria_db = Categorias.objects.get(categoria="notícias")
    #todas_postagens = Postagens.objects.all().filter(disponivel=True).select_related("fk_rss").\
    #    select_related("fk_rss__fk_sites").filter(fk_rss__disponivel=True).order_by("-horario_postagem_site")

    todas_postagens = Postagens.objects.select_related("fk_rss").filter(disponivel=True).filter(
        fk_rss__disponivel=True).prefetch_related("fk_rss__categorias").filter(
        fk_rss__categorias__categoria=categoria_db).order_by("-horario_postagem_site")

    paginator = Paginator(todas_postagens, 20)

    try:
        postagens = paginator.page(pagina)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)

    serializedpage = {}

    pythonserializer = serializers.get_serializer("python")()
    serializedpage["object_list"] = pythonserializer.serialize(postagens.object_list,
                                                               fields=('fk_rss', 'titulo', 'link', 'texto',
                                                                       'data_adicionado', 'data_modificado',
                                                                       'horario_postagem_site', 'fk_imagem'),
                                                               use_natural_foreign_keys=True,
                                                               use_natural_primary_keys=True)
    return JsonResponse(serializedpage)


@csrf_exempt
def get_last_news_by_site(request, id_site, pagina):
    todas_postagens = Postagens.objects.select_related("fk_rss__fk_sites").filter(fk_rss__fk_sites=id_site).filter(
        disponivel=True).select_related("fk_rss").filter(fk_rss__disponivel=True).order_by("-horario_postagem_site")

    paginator = Paginator(todas_postagens, 20)

    try:
        postagens = paginator.page(pagina)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)

    serializedpage = {}

    pythonserializer = serializers.get_serializer("python")()
    serializedpage["object_list"] = pythonserializer.serialize(postagens.object_list,
                                                               fields=('fk_rss', 'titulo', 'link', 'texto',
                                                                       'data_adicionado', 'data_modificado',
                                                                       'horario_postagem_site'))
    return JsonResponse(serializedpage)


@csrf_exempt
def get_last_news_by_category(request, categoria, pagina):
    categoria_db = Categorias.objects.get(categoria=categoria)
    todas_postagens = Postagens.objects.select_related("fk_rss").prefetch_related(
        "fk_rss__categorias").filter(fk_rss__categorias__categoria=categoria_db).order_by("-horario_postagem_site")

    paginator = Paginator(todas_postagens, 20)

    try:
        postagens = paginator.page(pagina)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)

    serializedpage = {}

    pythonserializer = serializers.get_serializer("python")()
    serializedpage["object_list"] = pythonserializer.serialize(postagens.object_list,
                                                               fields=('fk_rss', 'titulo', 'link', 'texto',
                                                                       'data_adicionado', 'data_modificado',
                                                                       'horario_postagem_site'))
    return JsonResponse(serializedpage)


@csrf_exempt
def criar_usuario_rest(request):
    if request.method == "POST":
        usuario_criado = {}
        if request.POST.get("metodo") == "com_senha":
            user, verifica = User.objects.create_user(username=request.POST.get("email"),
                                                      email=request.POST.get("email"),
                                                      password=request.POST.get("senha"))
            if verifica:
                usuario_criado["status"] = True
                usuario_criado["mensagem"] = "Usuário criado com sucesso!"
            else:
                usuario_criado = False
                usuario_criado["mensagem"] = "O usuário já existe."
        elif request.POST.get("metodo") == "facebook":
            user, verifica_u = User.objects.create_user(username=request.POST.get("email"),
                                                        email=request.POST.get("email"))
            try:
                provider = ProvedoresDeLogin.objects.get(nome="facebook")
                if verifica_u:
                    user, verifica_p = ProvidersUser.objects.get_or_create(key_o_auth=request.POST.get("id_facebook"),
                                                                           defaults={"fk_provedor": provider,
                                                                                     "fk_usuario": user})
                    if verifica_p:
                        usuario_criado["status"] = True
                        usuario_criado["mensagem"] = "Usuário criado com sucesso!"
                    else:
                        usuario_criado = False
                        usuario_criado["mensagem"] = "O usuário já existe."
            except ProvedoresDeLogin.DoesNotExist:
                usuario_criado = False
                usuario_criado["mensagem"] = "O provedor de login não está cadastrado: facebook"
            else:
                usuario_criado = False
                usuario_criado["mensagem"] = "O usuário já existe."
        return JsonResponse(usuario_criado)
    else:
        return HttpResponse("Método não suportado")


@csrf_exempt
def logar_rest(request):
    if request.method == "POST":
        resposta = {"dados": None, "erro": None}
        metodo = request.POST.get("metodo")
        if metodo == "com_senha":
            email = request.POST.get("email")
            senha = request.POST.get("senha")
            user = authenticate(username=email, password=senha)
            if user is not None:
                if user.is_active:
                    token = TokenLogin(fk_usuario=user)
                    token.save()
                    dados = {
                        "id_user": user.id,
                        "email": user.email,
                        "nome": user.name,
                        "token": token.id_token,
                    }
                    resposta["dados"] = dados
                    resposta["status"] = True
                    return JsonResponse(resposta)
                else:
                    resposta["status"] = False
                    resposta["erro"] = "O seu login está desativado, entre em contato com o administrador"
                    return JsonResponse(resposta)
            else:
                resposta["status"] = False
                resposta["erro"] = "O seu login e/ou sua senha estão incorretos"
                return JsonResponse(resposta)
        elif metodo == "facebook":
            id_facebook = request.POST.get("id_facebook")
            try:
                usuario = ProvidersUser.objects.select_related("fk_usuario").get(key_o_auth=id_facebook)
                token = TokenLogin(fk_usuario=usuario.fk_usuario)
                token.save()
                dados = {
                    "id_user": usuario.fk_usuario.id,
                    "email": usuario.fk_usuario.email,
                    "nome": usuario.fk_usuario.name,
                    "token": token.id_token,
                }
                resposta["id_user"] = dados
                resposta["status"] = True
                return JsonResponse(resposta)
            except ProvidersUser.DoesNotExist:
                resposta["status"] = False
                resposta["erro"] = "O seu usuário não existe. Vá na tela criar conta."
                return JsonResponse(resposta)
    else:
        return HttpResponse("Método não suportado")
