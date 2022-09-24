# -*- coding: utf-8 -*-

# Caching
# https://docs.djangoproject.com/en/1.11/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
