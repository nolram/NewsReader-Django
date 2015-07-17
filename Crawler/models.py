from django.db import models
from sorl.thumbnail import ImageField

class Sites(models.Model):
    id_sites = models.AutoField(primary_key=True)

    titulo = models.CharField(max_length=150, db_index=True)
    descricao = models.TextField()
    link = models.URLField(db_index=True, max_length=600)

    fk_logo = models.ForeignKey("Imagens", null=True)

    idioma = models.CharField(max_length=30)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} - {1}".format(self.titulo, self.link)


class SitesCategorias(models.Model):
    id_sites_categorias = models.AutoField(primary_key=True)
    fk_site = models.ForeignKey("Sites", related_name="fk_site")
    fk_categoria = models.ForeignKey("Categorias", related_name="fk_categoria")

    class Meta:
        unique_together = (("fk_site", "fk_categoria"),)

    def __str__(self):
        return "{0} - {1}".format(self.fk_site.titulo, self.fk_categoria.categoria)


class LinksRSS(models.Model):
    id_links_rss = models.AutoField(primary_key=True)
    fk_sites = models.ForeignKey("Sites")

    link_rss = models.URLField(db_index=True, max_length=600)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} - {1}".format(self.fk_sites.titulo, self.link_rss)


class RSSCategorias(models.Model):
    id_rss_categorias = models.AutoField(primary_key=True)
    fk_rss = models.ForeignKey("LinksRSS", related_name="fk_rss")
    fk_categoria = models.ForeignKey("Categorias", related_name="fk_categoria_rss")

    class Meta:
        unique_together = (("fk_rss", "fk_categoria"),)

    def __str__(self):
        return "{0} - {1}".format(self.fk_site.titulo, self.fk_categoria.categoria)


class Postagens(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    fk_rss = models.ForeignKey("LinksRSS")

    titulo = models.CharField(max_length=500)
    link = models.URLField(db_index=True, max_length=600, unique=True)
    link_origi = models.URLField(db_index=True, max_length=700, null=True, unique=True)
    texto = models.TextField(null=True)

    fk_imagem = models.ForeignKey("Imagens", related_name="img_postagem", null=True)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    horario_postagem_site = models.DateTimeField(null=True)

    def __str__(self):
        return "{0} - {1}".format(self.fk_site.titulo, self.titulo)


class Imagens(models.Model):
    id_imagem = models.AutoField(primary_key=True)
    img_cover = ImageField(null=True)
    data_inserido = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)
    img_link_orig = models.URLField(max_length=700, db_index=True, unique_for_year=True)

    def __str__(self):
        return "{0}".format(self.img_link_orig)


class TagsPostagens(models.Model):
    id_tags_postagens = models.AutoField(primary_key=True)
    fk_postagem = models.ForeignKey("Postagens", related_name="tp_postagem")
    fk_tag = models.ForeignKey("Tags", related_name="tp_tags")

    class Meta:
        unique_together = (("fk_postagem", "fk_tag"),)

    def __str__(self):
        return "{0} - {1}".format(self.fk_postagem.titulo, self.fk_tag.tag)


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
