from django.contrib import admin
from .models import ProvedoresDeLogin, UsuariosProvedor


admin.site.register(ProvedoresDeLogin)
admin.site.register(UsuariosProvedor)