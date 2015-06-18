# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0003_auto_20150608_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSSCategorias',
            fields=[
                ('id_rss_categorias', models.AutoField(primary_key=True, serialize=False)),
                ('fk_categoria', models.ForeignKey(to='Crawler.Categorias', related_name='fk_categoria_rss')),
                ('fk_rss', models.ForeignKey(to='Crawler.LinksRSS', related_name='fk_rss')),
            ],
        ),
        migrations.AddField(
            model_name='postagens',
            name='horario_postagem_site',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='postagens',
            name='img_cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postagens',
            name='img_thumbnail_min',
            field=models.ImageField(width_field=50, height_field=50, null=True, upload_to=''),
        ),
        migrations.AlterUniqueTogether(
            name='sitescategorias',
            unique_together=set([('fk_site', 'fk_categoria')]),
        ),
        migrations.AlterUniqueTogether(
            name='tagspostagens',
            unique_together=set([('fk_postagem', 'fk_tag')]),
        ),
        migrations.AlterUniqueTogether(
            name='rsscategorias',
            unique_together=set([('fk_rss', 'fk_categoria')]),
        ),
    ]
