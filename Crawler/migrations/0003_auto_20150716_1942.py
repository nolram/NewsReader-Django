# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0002_auto_20150716_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagens',
            name='img_link_orig',
            field=models.URLField(unique_for_year=True, db_index=True, max_length=700),
        ),
    ]
