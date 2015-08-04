from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', "Site.views.index"),
                       url(r'^login/$', 'Site.views.pag_login'),
                       url(r'^logout/$', 'Site.views.logout_view'),
                       url(r'^last_news/(?P<pagina>[0-9]+)/$', "Site.views.get_last_news"),
                       url(r'^post/(?P<id_postagem>[0-9]+)/$', "Site.views.pag_postagem"),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^get_last_news_by_site/(?P<id_site>[0-9]+)/(?P<pagina>[0-9]+)/$',
                           "Site.views.get_last_news_by_site"),
                       url(r'^get_last_news_by_category/(?P<categoria>\w+)/(?P<pagina>[0-9]+)/$',
                           "Site.views.get_last_news_by_category"),

                       url(r'^search/', include('haystack.urls')),

                       url(r'^login_rest/$', 'Site.views.logar_rest'),
                       url(r'^criar_usuario_rest/$', 'Site.views.criar_usuario_rest'))\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
