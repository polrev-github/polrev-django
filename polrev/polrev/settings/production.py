import os
from dotenv import load_dotenv

from .base import *

if not os.environ.get("IN_DOCKER"):
    dotenv_path = os.path.join(BASE_DIR, '../config/.prod.env')
    load_dotenv(dotenv_path)

from .common import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")

try:
    from .local import *
except ImportError:
    pass
