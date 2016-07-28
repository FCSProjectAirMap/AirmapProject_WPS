from .partials import *

DEBUG = False

ALLOWED_HOSTS = ["*", ]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = 'd2purq8hmwrb3i.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

MEDIA_URL = "https://d2purq8hmwrb3i.cloudfront.net/"
