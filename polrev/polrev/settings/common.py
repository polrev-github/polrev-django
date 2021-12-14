from .base import *

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
'''
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
'''

STATICFILES_LOCATION = 'static'
STATIC_ROOT = os.path.join(BASE_DIR, STATICFILES_LOCATION)
STATIC_URL = f'/{STATICFILES_LOCATION}/'
STATICFILES_STORAGE = 'polrev.storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIAFILES_LOCATION)
MEDIA_URL = f'/{MEDIAFILES_LOCATION}/'
DEFAULT_FILE_STORAGE = 'polrev.storages.MediaStorage'

AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", "")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")

AWS_QUERYSTRING_AUTH = False
#AWS_S3_SECURE_URLS = False
#AWS_S3_CUSTOM_DOMAIN = 'localhost:9000'

AWS_S3_OBJECT_PARAMETERS = {
    "ACL": "public-read",
   'CacheControl': 'max-age=86400',
}
