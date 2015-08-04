# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvidersUser',
            fields=[
                ('id_usuario_pro', models.AutoField(primary_key=True, serialize=False)),
                ('key_o_auth', models.CharField(max_length=700, db_index=True)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='assinatura',
            name='fk_plano',
        ),
        migrations.RemoveField(
            model_name='assinatura',
            name='id_usuario',
        ),
        migrations.AlterUniqueTogether(
            name='usuariosprovedor',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='usuariosprovedor',
            name='fk_provedor',
        ),
        migrations.RemoveField(
            model_name='usuariosprovedor',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='provedoresdelogin',
            name='key',
        ),
        migrations.RemoveField(
            model_name='provedoresdelogin',
            name='secret_key',
        ),
        migrations.DeleteModel(
            name='Assinatura',
        ),
        migrations.DeleteModel(
            name='Planos',
        ),
        migrations.DeleteModel(
            name='UsuariosProvedor',
        ),
        migrations.AddField(
            model_name='providersuser',
            name='fk_provedor',
            field=models.OneToOneField(to='Site.ProvedoresDeLogin', related_name='fk_provedor'),
        ),
        migrations.AddField(
            model_name='providersuser',
            name='fk_usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='fk_usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='providersuser',
            unique_together=set([('fk_usuario', 'fk_provedor')]),
        ),
    ]
