# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0005_sites_idioma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linksrss',
            name='link_rss',
            field=models.URLField(db_index=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='postagens',
            name='link',
            field=models.URLField(db_index=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='sites',
            name='link',
            field=models.URLField(db_index=True, max_length=600),
        ),
    ]
