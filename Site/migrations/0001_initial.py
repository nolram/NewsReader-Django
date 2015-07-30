# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id_usuario', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavoritosNoticiasUsuario',
            fields=[
                ('id_favoritos_noticias', models.AutoField(primary_key=True, serialize=False)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoNoticiasUsuario',
            fields=[
                ('id_historico_noticias', models.AutoField(primary_key=True, serialize=False)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('fk_noticia', models.ForeignKey(to='Crawler.Postagens', related_name='fk_noticia_histo_usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id_plano', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProvedoresDeLogin',
            fields=[
                ('id_provedor', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(db_index=True, max_length=50)),
                ('key', models.CharField(null=True, max_length=500)),
                ('secret_key', models.CharField(null=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UsuariosProvedor',
            fields=[
                ('id_usuario', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('key_o_auth', models.CharField(db_index=True, max_length=700)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('fk_provedor', models.ForeignKey(to='Site.ProvedoresDeLogin', related_name='fk_provedor')),
            ],
        ),
        migrations.CreateModel(
            name='ConteudoFavoritos',
            fields=[
                ('id_conteudo_favoritos', models.OneToOneField(primary_key=True, to='Site.FavoritosNoticiasUsuario', serialize=False)),
                ('titulo', models.CharField(max_length=500)),
                ('conteudo', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='historiconoticiasusuario',
            name='fk_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='fk_usua_histo'),
        ),
        migrations.AddField(
            model_name='favoritosnoticiasusuario',
            name='fk_noticia',
            field=models.ForeignKey(to='Crawler.Postagens', related_name='fk_noticia_fav_usuario'),
        ),
        migrations.AddField(
            model_name='favoritosnoticiasusuario',
            name='fk_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='fk_usua_fav'),
        ),
        migrations.AddField(
            model_name='assinatura',
            name='fk_plano',
            field=models.ForeignKey(to='Site.Planos', related_name='fk_plano_usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='usuariosprovedor',
            unique_together=set([('id_usuario', 'fk_provedor')]),
        ),
    ]
