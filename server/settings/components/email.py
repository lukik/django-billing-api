__author__ = 'Muchai Noah'

from server.settings import env
from server.settings.components.common import INSTALLED_APPS

# # EMAIL CONFIGURATION
# # ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# # If enabled, it logs the email to console. Neat!. And it takes precedence over EMAIL_HOST
# # EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
#
# Mail settings for local development using Mailhog
# ------------------------------------------------------------------------------
EMAIL_PORT = 1025
EMAIL_HOST = env('EMAIL_HOST', default='mailhog')


# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default='Billing API <noreply@billing-api.xyz>')
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[BILLING API:]')

# # Anymail with Mailgun
# INSTALLED_APPS += ['anymail', ]
# ANYMAIL = {
#     # MAILGUN_API_KEY: found under domain settings. starts with `key-#####`
#     'MAILGUN_API_KEY': env('DJANGO_MAILGUN_API_KEY'),
#
#     # MAILGUN_SENDER_DOMAIN: # Your domain is known hence the text `via mailgurn.org` does not appear in the email
#     'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
# }
# EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
