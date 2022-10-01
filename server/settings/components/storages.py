from server.settings import env
from typing import List

if env('DJANGO_ENVIRONMENT') == 'production':

    AWS_ACCESS_KEY_ID = env('DIGITAL_OCEAN_SPACES_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('DIGITAL_OCEAN_SPACES_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('DIGITAL_OCEAN_SPACES_BUCKET_NAME')
    AWS_S3_REGION_NAME = env('DIGITAL_OCEAN_SPACES_REGION_NAME')
    AWS_S3_ENDPOINT_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = env('DIGITAL_OCEAN_SPACES_STATIC_LOCATION')
    AWS_DEFAULT_ACL = None  # This allows the files to be set to private on Digital ocean
    STATICFILES_DIRS: List[str] = []
    STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'  # file located on root of the application
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'  # file located on root of the application
