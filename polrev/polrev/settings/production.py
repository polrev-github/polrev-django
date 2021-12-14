import os
from dotenv import load_dotenv

from .base import *

if not os.environ.get("IN_DOCKER"):
    dotenv_path = os.path.join(BASE_DIR, '../config/.prod.env')
    load_dotenv(dotenv_path)

from .common import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = os.environ.get("SECRET_KEY", "")