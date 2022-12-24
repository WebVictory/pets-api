"""
Django settings for pets_api project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=*y4259&19cy-^(a93u9)cge+-tj_&h^reuo1!gw)*c8r_hr@o'
#
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1","localhost"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',  # автоматическое удаление файлов после удлаения обьектов
    'rest_framework',
    'pets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pets_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pets_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = ''

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#указываем порт и кост для работы из консоли, подругому их не получить
DEFAULT_DOMAIN = ALLOWED_HOSTS[0]
DEFAULT_PORT = '80'

REST_FRAMEWORK = {
    #А.  Реализация API Key Authentication:
    'DEFAULT_PERMISSION_CLASSES': [
        'pets.permissions.APIKeyPermission'
    ],
    'DEFAULT_PAGINATION_CLASS': 'pets.pagination.CustomPagination',
    'PAGE_SIZE': 20,
    #если совпадает - обрабатываем запрос
    #несовпадает-401 Unauthorized без это функции код 403
    'EXCEPTION_HANDLER': 'pets.permissions.custom_exception_handler',
}

API_KEY = "API_KEY"
