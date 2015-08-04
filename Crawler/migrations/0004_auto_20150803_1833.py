# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0003_auto_20150803_1751'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rsscategorias',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='rsscategorias',
            name='fk_categoria',
        ),
        migrations.RemoveField(
            model_name='rsscategorias',
            name='fk_rss',
        ),
        migrations.RemoveField(
            model_name='postagens',
            name='fk_categoria',
        ),
        migrations.AddField(
            model_name='linksrss',
            name='categorias',
            field=models.ManyToManyField(related_name='rss_categorias', to='Crawler.Categorias'),
        ),
        migrations.DeleteModel(
            name='RSSCategorias',
        ),
    ]
