# -.- encoding:utf-8 -.-
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.http import Http404

from Crawler.models import Postagens

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

def get_last_news(request, numero):
    todas_postagens = Postagens.objects.all().order_by("-horario_postagem_site")

    paginator = Paginator(todas_postagens, 20)

    try:
        postagens = paginator.page(numero)
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


def get_last_news_by_site(request, pagina, id_site):
    todas_postagens = Postagens.objects.select_related("fk_rss__fk_sites").filter(fk_rss__fk_sites=id_site)\
        .order_by("-horario_postagem_site")

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


def get_last_news_by_category(request, pagina, id_site):
    todas_postagens = Postagens.objects.select_related("fk_rss__fk_sites").filter(fk_rss__fk_sites=id_site)\
        .order_by("-horario_postagem_site")

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
