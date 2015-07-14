# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0002_auto_20150714_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagens',
            name='link_origi',
            field=models.URLField(max_length=700, null=True, db_index=True),
        ),
    ]
