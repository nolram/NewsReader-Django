from django.db import models


class Sites(models.Model):
    id_sites = models.AutoField(primary_key=True)

    titulo = models.CharField(max_length=150, db_index=True)
    descricao = models.TextField()
    link = models.URLField(db_index=True)
    logo = models.ImageField(null=True)

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

    link_rss = models.URLField(db_index=True)

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
    fk_site = models.ForeignKey("Sites")

    titulo = models.CharField(max_length=500)
    link = models.URLField(db_index=True)
    texto = models.TextField(null=True)

    img_thumbnail_min = models.ImageField(null=True, height_field=50, width_field=50)
    img_cover = models.ImageField(null=True)

    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)

    horario_postagem_site = models.DateTimeField(null=True)

    def __str__(self):
        return "{0} - {1}".format(self.fk_site.titulo, self.titulo)


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
    categoria = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return "{0}".format(self.categoria)


class Tags(models.Model):
    id_tag = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100, db_index=True, unique=True)
    contador = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{0} - {1}".format(self.contador, self.tag)