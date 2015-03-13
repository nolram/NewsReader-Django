# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='contador',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag',
            field=models.CharField(unique=True, max_length=100, db_index=True),
            preserve_default=True,
        ),
    ]
