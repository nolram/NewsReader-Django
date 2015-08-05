# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Site', '0002_auto_20150801_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenLogin',
            fields=[
                ('id_token', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('data_login', models.DateTimeField(auto_now_add=True)),
                ('fk_usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
