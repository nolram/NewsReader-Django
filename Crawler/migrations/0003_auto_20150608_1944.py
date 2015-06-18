# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0002_auto_20150309_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='logo',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
