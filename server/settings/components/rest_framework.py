__author__ = 'Muchai Noah'
from datetime import timedelta
from server.settings import env
from server.settings.components import BASE_DIR

# DRF SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 40,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',
                                'rest_framework.filters.SearchFilter',
                                ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_VERSION': 'v1',  # If this is not in place then Swagger fails!!
    'ALLOWED_VERSIONS': ('v1', 'v2'),

    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}

#######################
# SIMPLE JWT
#######################
if env('DJANGO_ENVIRONMENT') == "production":
    # In Production the path is outside code directory
    jwt_signing_key = open(env("JWT_PRIVATE_KEY")).read()
    jwt_verifying_key = open(env("JWT_PUBLIC_KEY")).read()
else:
    # In Dev, Test, the path is within code directory
    jwt_signing_key = open(str(BASE_DIR) + env("JWT_PRIVATE_KEY")).read()
    jwt_verifying_key = open(str(BASE_DIR) + env("JWT_PUBLIC_KEY")).read()

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=env.int('JWT_EXPIRATION_DELTA')),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=env.int('JWT_REFRESH_TOKEN_DELTA')),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'RS256',
    'SIGNING_KEY': jwt_signing_key,  # Change this to another value so as to be independent of Django's secret key
    'VERIFYING_KEY': jwt_verifying_key,

    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

#########################
# Swagger Settings
#########################
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'APIS_SORTER': 'alpha',
    'SUPPORTED_SUBMIT_METHODS': ['get', 'post', 'put', 'delete', 'patch'],
    'OPERATIONS_SORTER': 'alpha',
    'TAGS_SORTER': 'alpha',
    'DOC_EXPANSION': 'None',
}

REDOC_SETTINGS = {
    'EXPAND_RESPONSES': '201',  # E.g. '200,201' or 'all'
    'PATH_IN_MIDDLE': 'False',
}

