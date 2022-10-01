__author__ = 'Muchai Noah'

from server.settings import env

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # Choices are: postgresql_psycopg2, mysql, sqlite3, oracle
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        # Database name or filepath if using 'sqlite3':
        'NAME': env('POSTGRES_DB'),

        # You don't need these settings if using 'sqlite3':
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('DJANGO_DATABASE_HOST'),
        'PORT': env.int('DJANGO_DATABASE_PORT'),
        'CONN_MAX_AGE': env.int('CONN_MAX_AGE', default=30),
    },
}
