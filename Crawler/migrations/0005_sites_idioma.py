# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0004_auto_20150616_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='idioma',
            field=models.CharField(default='pt-BR', max_length=30),
            preserve_default=False,
        ),
    ]
