from .base import *

DEBUG = False

# AWD S3 settings
AWS_S3_FILE_OVERWRITE = False
AWS_STORAGE_BUCKET_NAME = ENV.get("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = ENV.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = ENV.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

# general security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

if ENV.get("CSRF_TRUSTED_ORIGIN"):
    SRF_TRUSTED_ORIGINS = ENV.get("CSRF_TRUSTED_ORIGIN").split(",")

if ENV.get("SECURE_HSTS_SECONDS"):
    SECURE_HSTS_SECONDS = int(ENV.get("SECURE_HSTS_SECONDS"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

if ENV.get("SECURE_PROXY_SSL_HEADER"):
    # If we're behind a proxy, and the proxy is adding the SSL header, we need to tell Django to trust the header
    # Like heroku.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

