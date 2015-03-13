# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(serialize=False, primary_key=True)),
                ('categoria', models.CharField(max_length=100, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinksRSS',
            fields=[
                ('id_links_rss', models.AutoField(serialize=False, primary_key=True)),
                ('link_rss', models.URLField(db_index=True)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postagens',
            fields=[
                ('id_postagem', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('link', models.URLField(db_index=True)),
                ('texto', models.TextField(null=True)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id_sites', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=150, db_index=True)),
                ('descricao', models.TextField()),
                ('link', models.URLField(db_index=True)),
                ('logo', models.ImageField(null=True, upload_to=b'')),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SitesCategorias',
            fields=[
                ('id_sites_categorias', models.AutoField(serialize=False, primary_key=True)),
                ('fk_categoria', models.ForeignKey(related_name='fk_categoria', to='Crawler.Categorias')),
                ('fk_site', models.ForeignKey(related_name='fk_site', to='Crawler.Sites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id_tag', models.AutoField(serialize=False, primary_key=True)),
                ('tag', models.CharField(max_length=100, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagsPostagens',
            fields=[
                ('id_tags_postagens', models.AutoField(serialize=False, primary_key=True)),
                ('fk_postagem', models.ForeignKey(related_name='tp_postagem', to='Crawler.Postagens')),
                ('fk_tag', models.ForeignKey(related_name='tp_tags', to='Crawler.Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='postagens',
            name='fk_site',
            field=models.ForeignKey(to='Crawler.Sites'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linksrss',
            name='fk_sites',
            field=models.ForeignKey(to='Crawler.Sites'),
            preserve_default=True,
        ),
    ]
