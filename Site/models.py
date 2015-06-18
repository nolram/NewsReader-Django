from django.db import models
from django.contrib.auth.models import User


class UsuariosProvider(models.Model):
    id_usuario = models.ForeignKey(User, primary_key=True, unique=True)
    fk_provider = models.ForeignKey("Providers", related_name="fk_provider")
    id_provider = models.TextField(db_index=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0} - {1}".format(self.id_usuario.email, self.fk_provider.nome)


class Providers(models.Model):
    id_provider = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, db_index=True)
    key = models.CharField(max_length=500, null=True)
    secret_key = models.CharField(max_length=500, null=True)

    def __unicode__(self):
        return u"{0}".format(self.nome)