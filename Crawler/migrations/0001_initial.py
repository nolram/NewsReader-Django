# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100, db_index=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id_imagem', models.AutoField(primary_key=True, serialize=False)),
                ('img_cover', sorl.thumbnail.fields.ImageField(null=True, upload_to='')),
                ('data_inserido', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
                ('img_link_orig', models.URLField(max_length=700, db_index=True, unique_for_year=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinksRSS',
            fields=[
                ('id_links_rss', models.AutoField(primary_key=True, serialize=False)),
                ('link_rss', models.URLField(max_length=600, db_index=True)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postagens',
            fields=[
                ('id_postagem', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=500)),
                ('link', models.URLField(max_length=600, db_index=True, unique=True)),
                ('link_origi', models.URLField(max_length=700, null=True, db_index=True, unique=True)),
                ('texto', models.TextField(null=True)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
                ('horario_postagem_site', models.DateTimeField(null=True)),
                ('fk_imagem', models.ForeignKey(null=True, related_name='img_postagem', to='Crawler.Imagens')),
                ('fk_rss', models.ForeignKey(to='Crawler.LinksRSS')),
            ],
        ),
        migrations.CreateModel(
            name='RSSCategorias',
            fields=[
                ('id_rss_categorias', models.AutoField(primary_key=True, serialize=False)),
                ('fk_categoria', models.ForeignKey(related_name='fk_categoria_rss', to='Crawler.Categorias')),
                ('fk_rss', models.ForeignKey(related_name='fk_rss', to='Crawler.LinksRSS')),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id_sites', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, db_index=True)),
                ('descricao', models.TextField()),
                ('link', models.URLField(max_length=600, db_index=True)),
                ('idioma', models.CharField(max_length=30)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
                ('fk_logo', models.ForeignKey(null=True, to='Crawler.Imagens')),
            ],
        ),
        migrations.CreateModel(
            name='SitesCategorias',
            fields=[
                ('id_sites_categorias', models.AutoField(primary_key=True, serialize=False)),
                ('fk_categoria', models.ForeignKey(related_name='fk_categoria', to='Crawler.Categorias')),
                ('fk_site', models.ForeignKey(related_name='fk_site', to='Crawler.Sites')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id_tag', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=100, db_index=True, unique=True)),
                ('contador', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TagsPostagens',
            fields=[
                ('id_tags_postagens', models.AutoField(primary_key=True, serialize=False)),
                ('fk_postagem', models.ForeignKey(related_name='tp_postagem', to='Crawler.Postagens')),
                ('fk_tag', models.ForeignKey(related_name='tp_tags', to='Crawler.Tags')),
            ],
        ),
        migrations.AddField(
            model_name='linksrss',
            name='fk_sites',
            field=models.ForeignKey(to='Crawler.Sites'),
        ),
        migrations.AlterUniqueTogether(
            name='tagspostagens',
            unique_together=set([('fk_postagem', 'fk_tag')]),
        ),
        migrations.AlterUniqueTogether(
            name='sitescategorias',
            unique_together=set([('fk_site', 'fk_categoria')]),
        ),
        migrations.AlterUniqueTogether(
            name='rsscategorias',
            unique_together=set([('fk_rss', 'fk_categoria')]),
        ),
    ]
