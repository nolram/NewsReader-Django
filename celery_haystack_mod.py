__author__ = 'nolram'
from celery import Celery

app = Celery('celery_haystack')
app.config_from_object('django.conf:settings')