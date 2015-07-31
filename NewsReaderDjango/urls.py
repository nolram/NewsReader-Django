from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from Site.providers_login import FacebookLogin, TwitterLogin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', "Site.views.index"),
                       url(r'^login/$', 'Site.views.pag_login'),
                       url(r'^logout/$', 'Site.views.logout_view'),
                       url(r'^last_news/(?P<numero>[0-9]+)/$', "Site.views.get_last_news"),
                       url(r'^postagem/(?P<id_postagem>[0-9]+)/$', "Site.views.pag_postagem"),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^search/', include('haystack.urls')),

                       url(r'^rest-auth/', include('rest_auth.urls')),
                       url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
                       url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
                       url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login')
                       ) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
