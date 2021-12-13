from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    default_acl = "public-read"

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    default_acl = "public-read"
    file_overwrite = False

'''
from storages.backends.s3boto3 import S3ManifestStaticStorage

class ManifestS3Storage(S3ManifestStaticStorage):
    #location = "static"
    default_acl = "public-read"
    manifest_strict = False
'''