from storages.backends.s3boto3 import S3ManifestStaticStorage

class ManifestS3Storage(S3ManifestStaticStorage):
    #location = "static"
    default_acl = "public-read"
    manifest_strict = False