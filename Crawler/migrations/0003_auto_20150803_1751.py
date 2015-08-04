# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0002_auto_20150725_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='linksrss',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='postagens',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='postagens',
            name='fk_categoria',
            field=models.ForeignKey(null=True, related_name='fk_categoria_postagem', to='Crawler.Categorias'),
        ),
    ]
