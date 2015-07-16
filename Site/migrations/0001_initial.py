# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id_provider', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(db_index=True, max_length=50)),
                ('key', models.CharField(null=True, max_length=500)),
                ('secret_key', models.CharField(null=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UsuariosProvider',
            fields=[
                ('id_usuario', models.ForeignKey(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL, unique=True)),
                ('id_provider', models.TextField(db_index=True)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('fk_provider', models.ForeignKey(to='Site.Providers', related_name='fk_provider')),
            ],
        ),
    ]
