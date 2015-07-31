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

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iudhm*b^7!8ea5nrjgwz@m1(pkjq60acj0+9*h1_d6!!c(&yr3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

USING_SQLITE = False

ALLOWED_HOSTS = []

NO_SERVIDOR = True

# Application definition

SITE_ID = 1

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'Site',
    'Crawler',
    'sorl.thumbnail',
    'kronos',

    'rest_framework',
    'rest_framework.authtoken',

    'rest_auth',

    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

ROOT_URLCONF = 'NewsReaderDjango.urls'

WSGI_APPLICATION = 'NewsReaderDjango.wsgi.application'

if USING_SQLITE:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                'USER': '',
                'PASSWORD': '',
            }
    }
else:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'newsreader',
                'USER': 'flynadmin', #'postgres',
                'PASSWORD': 'flYnReadER2015', #'12345678',
            }
    }

TIMEOUT = 10000

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
if NO_SERVIDOR:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "static_root"),
    )
else:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

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

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

#KRONOS_PYTHONPATH = "/home/nolram/Virtualenv/py3_django/bin/python3"

if NO_SERVIDOR:
    KRONOS_POSTFIX = "> /opt/flyn_django/log_thread.log 2>&1 "
else:
    KRONOS_PREFIX = "source /home/nolram/Virtualenv/py3_django/bin/activate &&"
    KRONOS_POSTFIX = "> /home/nolram/log_thread.log 2>&1 "