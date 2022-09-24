"""
Billing API centric settings
"""
__author__ = 'Muchai Noah'

from server.settings import env

APP_NAME = env('APP_NAME')
URL_BILLING_API = env('URL_BILLING_API')
URL_EMAIL_VERIFICATION = f"{URL_BILLING_API}/{env('URL_EMAIL_VERIFICATION')}"
URL_PASSWORD_RESET = f"{URL_BILLING_API}/{env('URL_PASSWORD_RESET')}"
URL_TERMS_CONDITIONS = env('URL_TERMS_CONDITIONS')
URL_PRIVACY = env('URL_PRIVACY')
COPYRIGHT = 'BILLING API 2019'

# ##########################################
# Password Tokens Validity period (seconds)
# ##########################################
# Used for Email & Mobile Number Verification Tokens, Password Reset Token
USER_INPUT_CODE_LENGTH = env('USER_INPUT_CODE_LENGTH', default=6)
USER_INPUT_CODE_VALIDITY_PERIOD = env('USER_INPUT_CODE_VALIDITY_PERIOD', default=3600)
PASSWORD_RESET_TOKEN_VALIDITY_PERIOD = env('PASSWORD_RESET_TOKEN_VALIDITY_PERIOD', default=300)
