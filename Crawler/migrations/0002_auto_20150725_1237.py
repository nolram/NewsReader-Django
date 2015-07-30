# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagens',
            name='fk_imagem',
            field=models.ForeignKey(related_name='fk_imagem_postagem', null=True, to='Crawler.Imagens'),
        ),
    ]
