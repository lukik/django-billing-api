__author__ = 'Muchai Noah'
from datetime import timedelta
from kombu import Exchange, Queue
from server.settings import env
from server.settings.components.common import INSTALLED_APPS
from server.settings.components.redis import REDIS_URL, REDIS_DB_CELERY


# ##########################################
# CELERY
# http://docs.celeryproject.org/en/latest/userguide/configuration.html
# ##########################################
INSTALLED_APPS += ['server.taskapp.celery.CeleryConfig']

# Broker Settings
CELERY_BROKER_URL = f'{REDIS_URL}/{REDIS_DB_CELERY}'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_CREATE_MISSING_QUEUES = True

# List of modules to import when the Celery worker starts.
CELERY_IMPORTS = (

)
"""
The non-AMQP backends like Redis or SQS don’t support exchanges, so they require the exchange to have the same name as
the queue. Using this design ensures it will work for them as well.
source: https://docs.celeryproject.org/en/latest/userguide/routing.html
"""
# Name Placeholders
file_runner = "file_runner"

# Declare the exchanges
exchange_default = Exchange("billing_api_exchange", type='direct')

CELERY_TASK_QUEUES = (
    Queue(file_runner, exchange=exchange_default, routing_key=file_runner),
)

CELERY_TASK_ROUTES = (
    # Import school setup file
    {'partners.partner_import.import_partners': {'queue': file_runner}},

)

# Celery Beat Timing

CELERY_BEAT_SCHEDULE = {

}
