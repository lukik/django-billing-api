__author__ = 'Muchai Noah'

from server.settings import env

REDIS_HOST = env('REDIS_HOST', default='redis')
REDIS_PASS = env('REDIS_PASS', default='')
REDIS_PORT = env.int('REDIS_PORT', default=6379)
REDIS_URL = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}'
REDIS_DB_MAIN = env.int('REDIS_DB_MAIN')
REDIS_DB_CELERY = env.int('REDIS_DB_CELERY')
REDIS_DB_CELERY_RESULTS_BACKEND = env.int('REDIS_DB_CELERY_RESULTS_BACKEND')
REDIS_DB_CACHE = env.int('REDIS_DB_CACHE')
REDIS_DB_REDISEARCH = env.int('REDIS_DB_REDISEARCH')
