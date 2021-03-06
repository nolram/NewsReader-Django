from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User


class Sites(models.Model):

    id_sites = models.AutoField(primary_key=True)

    titulo = models.CharField(max_length=150, db_index=True)
    descricao = models.TextField()
    link = models.URLField(db_index=True, max_length=600)

    fk_logo = models.ForeignKey("Imagens", null=True)

    idioma = models.CharField(max_length=30)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    categorias = models.ManyToManyField("Categorias", related_name="sites_categorias")

    def natural_key(self):
        return self.titulo, self.link

    def __str__(self):
        return "{0} - {1}".format(self.titulo, self.link)


class LinksRSS(models.Model):
    id_links_rss = models.AutoField(primary_key=True)
    fk_sites = models.ForeignKey("Sites")

    link_rss = models.URLField(db_index=True, max_length=600)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    disponivel = models.BooleanField(default=True)

    categorias = models.ManyToManyField("Categorias", related_name="rss_categorias")

    def natural_key(self):
        return self.link_rss, self.fk_sites.titulo

    def __str__(self):
        return "{0} - {1}".format(self.fk_sites.titulo, self.link_rss)


class Postagens(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    fk_rss = models.ForeignKey("LinksRSS", related_name="fk_rss_postagem")

    titulo = models.CharField(max_length=500)
    link = models.URLField(db_index=True, max_length=700, unique=True)
    link_origi = models.URLField(db_index=True, max_length=700, null=True, unique=True)
    texto = models.TextField(null=True)

    fk_imagem = models.ForeignKey("Imagens", related_name="fk_imagem_postagem", null=True)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    horario_postagem_site = models.DateTimeField(null=True)

    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return "{0} - {1}".format(self.fk_rss.fk_sites.titulo, self.titulo)


class Imagens(models.Model):
    id_imagem = models.AutoField(primary_key=True)
    img_cover = ImageField(null=True)
    data_inserido = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)
    img_link_orig = models.URLField(max_length=700, db_index=True, unique=True)

    def natural_key(self):
        return self.img_link_orig, self.id_imagem

    def __str__(self):
        return "{0}".format(self.img_link_orig)


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return "{0}".format(self.categoria)


class Tags(models.Model):
    id_tag = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100, db_index=True, unique=True)
    contador = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{0} - {1}".format(self.contador, self.tag)


class TagsPostagens(models.Model):
    id_tags_postagens = models.AutoField(primary_key=True)
    fk_postagem = models.ForeignKey("Postagens", related_name="tp_postagem")
    fk_tag = models.ForeignKey("Tags", related_name="tp_tags")

    class Meta:
        unique_together = (("fk_postagem", "fk_tag"),)

    def __str__(self):
        return "{0} - {1}".format(self.fk_postagem.titulo, self.fk_tag.tag)
