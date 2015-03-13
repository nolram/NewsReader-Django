# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id_provider', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=50, db_index=True)),
                ('key', models.CharField(max_length=500, null=True)),
                ('secret_key', models.CharField(max_length=500, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsuariosProvider',
            fields=[
                ('id_usuario', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id_provider', models.TextField(db_index=True)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('fk_provider', models.ForeignKey(related_name='fk_provider', to='Site.Providers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
