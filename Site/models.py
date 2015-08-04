from django.db import models
from django.contrib.auth.models import User
from Crawler.models import Postagens


class ProvidersUser(models.Model):
    id_usuario_pro = models.AutoField(primary_key=True)
    fk_usuario = models.OneToOneField(User, related_name="fk_usuario")
    fk_provedor = models.OneToOneField("ProvedoresDeLogin", related_name="fk_provedor")
    key_o_auth = models.CharField(max_length=700, db_index=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"{0} - {1}".format(self.id_usuario.email, self.fk_provider.nome)

    class Meta:
        unique_together = (("fk_usuario", "fk_provedor"),)


class ProvedoresDeLogin(models.Model):
    id_provedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return u"{0}".format(self.nome)


class HistoricoNoticiasUsuario(models.Model):
    id_historico_noticias = models.AutoField(primary_key=True)
    fk_noticia = models.ForeignKey(Postagens, related_name="fk_noticia_histo_usuario")
    fk_usuario = models.ForeignKey(User, related_name="fk_usua_histo")
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"{0} - {1}".format(self.fk_usuario.username, self.fk_noticia.titulo)


class FavoritosNoticiasUsuario(models.Model):
    id_favoritos_noticias = models.AutoField(primary_key=True)
    fk_noticia = models.ForeignKey(Postagens, related_name="fk_noticia_fav_usuario")
    fk_usuario = models.ForeignKey(User, related_name="fk_usua_fav")
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"{0} - {1}".format(self.fk_usuario.username, self.fk_noticia.titulo)


class ConteudoFavoritos(models.Model):
    id_conteudo_favoritos = models.OneToOneField(FavoritosNoticiasUsuario, primary_key=True)
    titulo = models.CharField(max_length=500)
    conteudo = models.TextField()

    def __str__(self):
        return u"{0} - {1}".format(self.id_conteudo_favoritos.fk_usuario,
                                   self.id_conteudo_favoritos.fk_noticia.titulo)