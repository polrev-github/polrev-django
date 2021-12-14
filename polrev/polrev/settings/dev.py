import os
from dotenv import load_dotenv

from .base import *

if not os.environ.get("IN_DOCKER"):
    dotenv_path = os.path.join(BASE_DIR, '../config/.dev.env')
    load_dotenv(dotenv_path)

from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mqmsq70)870^-0&+#^8u@5(dbj@o-yj9=@!f90)7s$ei##n_z7'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
