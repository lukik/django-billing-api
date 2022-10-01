# -*- coding: utf-8 -*-

"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

To change settings file:
`DJANGO_ENVIRONMENT=production python manage.py runserver`
"""

# from os import environ
# # Managing environment via DJANGO_ENVIRONMENT variable:
# environ.setdefault('DJANGO_ENVIRONMENT', 'development')
# ENV = environ['DJANGO_ENVIRONMENT']

import environ

from split_settings.tools import optional, include

ROOT_DIR = environ.Path(__file__) - 3  # (billing_api/config/settings/base.py - 3 = billing_api/)
APPS_DIR = ROOT_DIR.path('billing_api')

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# .env_dev file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env_dev file,
    # that is to say variables from the .env_dev files will only be used if not defined
    # as environment variables.
    ENV_FILE = env.str('PATH_ENV_FILE', default='')
    if ENV_FILE:
        env_file = ENV_FILE
    else:
        env_file = str(ROOT_DIR.path('config/.env'))

    env.read_env(env_file)
    print('PATH_ENV_FILE : {}'.format(env_file))


base_settings = [
    'components/common.py',
    'components/billing_api.py',
    'components/sentry.py',
    'components/caches.py',
    'components/database.py',
    'components/redis.py',
    'components/rest_framework.py',
    'components/file_paths.py',
    'components/celery.py',
    'components/email.py',
    'components/storages.py',

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    f'environments/{env("DJANGO_ENVIRONMENT")}.py',

    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
