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
            name='link',
            field=models.URLField(unique=True, max_length=600, db_index=True),
        ),
        migrations.AlterField(
            model_name='postagens',
            name='link_origi',
            field=models.URLField(unique=True, null=True, db_index=True, max_length=700),
        ),
    ]
