from django.conf.urls import url
from django.contrib import admin

from Site import views

admin.autodiscover()

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^$', views.index),
               url(r'^login/$', views.pag_login),
               url(r'^logout/$', views.logout_view),
               url(r'^last_news/(?P<pagina>[0-9]+)', views.get_last_news),
               url(r'^post/(?P<id_postagem>[0-9]+)/$', views.pag_postagem),

               url(r'^get_last_news_by_site/(?P<id_site>[0-9]+)/(?P<pagina>[0-9]+)/$',
                           views.get_last_news_by_site),
               url(r'^get_last_news_by_category/(?P<categoria>\w+)/(?P<pagina>[0-9]+)/$',
                           views.get_last_news_by_category),
               #url(r'^pesquisa/$', "views.pesquisa_pagina"),

               #url(r'^search/', include('haystack.urls')),

               url(r'^login_rest/$', views.logar_rest),
               url(r'^criar_usuario_rest/$', views.criar_usuario_rest)]
              #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
