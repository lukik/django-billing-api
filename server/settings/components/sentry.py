# -*- coding: utf-8 -*-

# Logging
# https://docs.djangoproject.com/en/1.11/topics/logging/
# https://docs.sentry.io/clients/python/integrations/django/

from server.settings import env

if env.str('DJANGO_ENVIRONMENT') == "production":

    import sentry_sdk
    import git
    import logging
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.celery import CeleryIntegration
    from sentry_sdk.integrations.redis import RedisIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    repo = git.Repo(search_parent_directories=True)

    sentry_logging = LoggingIntegration(
        level=logging.ERROR,
        event_level=logging.ERROR
    )

    sentry_sdk.init(
        dsn=env.str('SENTRY_DSN'),
        environment=env.str('DJANGO_ENVIRONMENT'),
        release=repo.head.object.hexsha,
        integrations=[DjangoIntegration(), CeleryIntegration(), RedisIntegration(), sentry_logging]
    )
