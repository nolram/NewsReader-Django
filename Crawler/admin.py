from django.contrib import admin
from .models import Tags, Sites, Postagens, LinksRSS, Categorias, TagsPostagens, Imagens

admin.site.register(Tags)
admin.site.register(Sites)
admin.site.register(Postagens)
admin.site.register(LinksRSS)
admin.site.register(Categorias)
admin.site.register(TagsPostagens)
admin.site.register(Imagens)
