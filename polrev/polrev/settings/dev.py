import os

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static', 'dist'),
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mqmsq70)870^-0&+#^8u@5(dbj@o-yj9=@!f90)7s$ei##n_z7'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DO NOT use on production, test key is available in the URL below
# https://developers.google.com/recaptcha/docs/faq
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]
