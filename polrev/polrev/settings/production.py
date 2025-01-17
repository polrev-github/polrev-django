import os

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", "")

CSRF_TRUSTED_ORIGINS = ['https://*.pol-rev.com']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
