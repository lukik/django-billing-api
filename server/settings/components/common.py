# -*- coding: utf-8 -*-

"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from typing import Tuple

from server.settings import env, ROOT_DIR
from server.settings.components import BASE_DIR  # , config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
SECRET_KEY = env('DJANGO_SECRET_KEY')

# Application definition:
EXTERNAL_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # Useful templates tags:
    'corsheaders',
    'rest_framework',  # Django Rest Framework
    'auditlog',  # Track Model Changes

)

BILLING_API_APPS = (

)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = list(EXTERNAL_APPS) + list(BILLING_API_APPS)

MIDDLEWARE: Tuple[str, ...] = (

    # Django:
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # cors
    'django.middleware.common.CommonMiddleware',  # cors
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Audit Log. This is required if you want to capture the actor in the audit log
    'auditlog.middleware.AuditlogMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('en', 'English'),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Templates
# https://docs.djangoproject.com/en/1.11/ref/templates/api

TEMPLATES = [{
    'APP_DIRS': True,
    # 'loaders': (
    #         'multisite.template.loaders.filesystem.Loader',
    #         'django.template.loaders.app_directories.Loader',
    # ),
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # Contains plain text templates, like `robots.txt`:
        BASE_DIR.joinpath('server', 'templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            # default template context processors
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
        ],
    },

}]

# Media files
# Media-root is commonly changed in production
# (see development.py and production.py).

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Django default authentication system.
# https://docs.djangoproject.com/en/1.11/topics/auth/

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Custom Admin URL, use {% url 'admin:index' %}
ADMIN_URL = env('DJANGO_ADMIN_URL')


# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(ROOT_DIR('fixtures')),
)

# Allow All CORS
CORS_ALLOW_ALL_ORIGINS = True

# Cross Origin Resource sharing
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8010',
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'Authorization',
    'Access-Control-Allow-Headers',
    'X-CURRENT-ROLE-ID',
    'Content-Type',
    'ACTIVE-PROFILE-TYPE'
)

