# -*- coding: utf-8 -*-

"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""
from typing import List
from server.settings import env, ROOT_DIR
from server.settings.components.common import INSTALLED_APPS

# Production flags:

DEBUG = True

ALLOWED_HOSTS = [
    # TODO: check production hosts
    env('DOMAIN_NAME'),
]


# # Staticfiles
# This are now defined under /server/settings/components/storages

# # Mediafiles
# This are now defined under /server/settings/components/storages


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.MinimumLengthValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.CommonPasswordValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.NumericPasswordValidator'.format(_PASS),
    },
]


# Security
# https://docs.djangoproject.com/en/1.11/topics/security/

SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'

