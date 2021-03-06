"""
Django settings for NewsReaderDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
from datetime import timedelta

from celery import Celery

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iudhm*b^7!8ea5nrjgwz@m1(pkjq60acj0+9*h1_d6!!c(&yr3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

NO_SERVIDOR = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'djcelery',

    'Site',
    'Crawler',
    'sorl.thumbnail',
    #'kronos',
)

#HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

BROKER_TRANSPORT = "memory"
CELERY_ALWAYS_EAGER = True
CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#        'URL': 'http://127.0.0.1:9200/',
#        'INDEX_NAME': 'haystack',
#    },
#}

ROOT_URLCONF = 'NewsReaderDjango.urls'

WSGI_APPLICATION = 'NewsReaderDjango.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER':  'postgres',
        'PASSWORD': 'docker',
        'HOST': 'db',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_crawler',
        },
    },
}

TIMEOUT = 10000

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
if NO_SERVIDOR:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
#if NO_SERVIDOR:
#    STATICFILES_DIRS = (
#        os.path.join(BASE_DIR, "static_root"),
#    )
#else:
#    STATICFILES_DIRS = (
#        os.path.join(BASE_DIR, "Site/static"),
#    )

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,  'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGIN_URL = '/login/'

#BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

#KRONOS_PYTHONPATH = "/home/nolram/Virtualenv/py3_django/bin/python3"

#if NO_SERVIDOR:
#    KRONOS_POSTFIX = "> /opt/flyn_django/log_thread.log 2>&1 "
#else:
#    KRONOS_PREFIX = "source /home/nolram/Virtualenv/py3_django/bin/activate &&"
#    KRONOS_POSTFIX = "> /home/nolram/log_thread.log 2>&1 "