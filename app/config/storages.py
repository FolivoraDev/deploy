from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = 'media'
    AWS_DEFAULT_ACL = 'private'


class StaticStorage(S3Boto3Storage):
    location = 'static'
    AWS_DEFAULT_ACL = 'public-read'

