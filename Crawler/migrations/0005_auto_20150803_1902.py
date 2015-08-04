# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0004_auto_20150803_1833'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sitescategorias',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='sitescategorias',
            name='fk_categoria',
        ),
        migrations.RemoveField(
            model_name='sitescategorias',
            name='fk_site',
        ),
        migrations.AddField(
            model_name='sites',
            name='categorias',
            field=models.ManyToManyField(to='Crawler.Categorias', related_name='sites_categorias'),
        ),
        migrations.DeleteModel(
            name='SitesCategorias',
        ),
    ]
