from .base import *

from django.contrib.messages import constants as messages

IN_DOCKER = os.environ.get("IN_DOCKER")

POLREV_DOMAIN = os.environ.get('POLREV_DOMAIN', 'localhost')

if not IN_DOCKER:
    os.environ['POSTGRES_HOST'] = 'localhost'
    os.environ['REDIS_HOST'] = 'localhost'
    #AWS_S3_ENDPOINT_URL=http://localhost:9000
    os.environ['AWS_S3_ENDPOINT_URL'] = 'http://localhost:9000'
    #AWS_BACKUP_S3_ENDPOINT_URL=http://localhost:9000
    os.environ['AWS_BACKUP_S3_ENDPOINT_URL'] = 'http://localhost:9000'


# Application definition

INSTALLED_APPS = [
    'wagtail.contrib.search_promotions',
    'wagtail.contrib.settings',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'generic_chooser',

    # AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'avatar',

    'django_comments_xtd',
    'django_comments',

    'crispy_forms',
    'crispy_bootstrap5',

    "django_bootstrap5",

    "colorfield",

    #"captcha",
    #"wagtailcaptcha",

    'wagtail.contrib.sitemaps',
    'wagtail.contrib.routable_page',
    #'wagtail.contrib.modeladmin',
    'wagtail_modeladmin',

    'django_social_share',
    'puput',
    #'colorful', # something else must be importing this
    'wagtailmarkdown',
    'modelcluster',
    'taggit',
    'wagtailautocomplete',

    'ls.joyous',
    'tz_detect',
    
    #'mjml',
    #'birdsong',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'storages',
    'dbbackup',  # django-dbbackup
    'corsheaders',

    'django_celery_beat',

    'polrev',
    'home',
    'info',
    'blog',
    'forms',
    'search',
    'accounts',
    'events',
    #'mailer',
    'campaigns',
    'slack_invite',
    'areas',
    'offices',
    'parties',

    # Portals
    'portals.volunteer',
    'portals.run',

    # Reddit
    'reddit',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'tz_detect.middleware.TimezoneMiddleware',

    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'polrev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            os.path.join(BASE_DIR, 'info', 'templates'),
            os.path.join(BASE_DIR, 'accounts', 'templates'),
            os.path.join(BASE_DIR, 'blog', 'templates'),
            os.path.join(BASE_DIR, 'events', 'templates'),
            os.path.join(BASE_DIR, 'mailer', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.blog'
            ],
        },
    },
]

WSGI_APPLICATION = 'polrev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("POSTGRES_HOST", ""),
        "NAME": os.environ.get("POSTGRES_DB", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "USER": os.environ.get("POSTGRES_USER", ""),
    }
}

MIGRATION_MODULES = {
    'puput': 'polrev.migrations.puput',
    'avatar': 'polrev.migrations.avatar',
    'joyous': 'polrev.migrations.joyous',
    'birdsong': 'polrev.migrations.birdsong'
}

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    #os.path.join(PROJECT_DIR, 'static'),
]

# Wagtail settings

WAGTAIL_SITE_NAME = "The Political Revolution"
#WAGTAILADMIN_BASE_URL = f"https://{os.environ.get('POLREV_DOMAIN', 'localhost')}"
WAGTAILADMIN_BASE_URL = f"https://{POLREV_DOMAIN}/admin"
# Search
# https://docs.wagtail.io/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}

WAGTAILMARKDOWN = {
    "autodownload_fontawesome": False,
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
#BASE_URL = 'https://pol-rev.com'
BASE_URL = f"https://{POLREV_DOMAIN}"

PUPUT_AS_PLUGIN = True
PUPUT_COMMENTS_PROVIDER = "puput.comments.DjangoCommentsProvider"
PUPUT_ENTRY_MODEL = 'blog.models.EntryAbstract'

WAGTAILEMBEDS_FINDERS = [
    {
        'class': 'wagtail.embeds.finders.oembed'
    }
]

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 8
COMMENTS_XTD_CONFIRM_EMAIL = True

EMAIL_HOST = "smtp.mail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "alias@mail.com"
EMAIL_HOST_PASSWORD = "yourpassword"
DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@yourdomain>"

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
'''
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
'''

STATICFILES_LOCATION = 'static'
STATIC_ROOT = os.path.join(BASE_DIR, STATICFILES_LOCATION)
STATIC_URL = f'/{STATICFILES_LOCATION}/'
#STATICFILES_STORAGE = 'polrev.storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIAFILES_LOCATION)
MEDIA_URL = f'/{MEDIAFILES_LOCATION}/'
#DEFAULT_FILE_STORAGE = 'polrev.storages.MediaStorage'

STORAGES = {
    "default": {
        "BACKEND": "polrev.storages.MediaStorage",
        "OPTIONS": {
          #...your_options_here
        },
    },
    "staticfiles": {
        "BACKEND": "polrev.storages.StaticStorage",
        "OPTIONS": {
          #...your_options_here
        },
    },
}

AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", "")
#print(AWS_S3_ENDPOINT_URL)
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")

AWS_IS_GZIPPED = True
AWS_QUERYSTRING_AUTH = False
#AWS_S3_SECURE_URLS = False
#AWS_S3_CUSTOM_DOMAIN = 'localhost:9000'

AWS_S3_OBJECT_PARAMETERS = {
    "ACL": "public-read",
   'CacheControl': 'max-age=86400',
}

AWS_BACKUP_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", "")
AWS_BACKUP_ACCESS_KEY_ID = os.environ.get("AWS_BACKUP_ACCESS_KEY_ID", "")
AWS_BACKUP_SECRET_ACCESS_KEY = os.environ.get("AWS_BACKUP_SECRET_ACCESS_KEY", "")
AWS_BACKUP_STORAGE_BUCKET_NAME = os.environ.get("AWS_BACKUP_STORAGE_BUCKET_NAME", "")

DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DBBACKUP_STORAGE_OPTIONS = {
    'endpoint_url': AWS_BACKUP_S3_ENDPOINT_URL,
    'access_key': AWS_BACKUP_ACCESS_KEY_ID,
    'secret_key': AWS_BACKUP_SECRET_ACCESS_KEY,
    'bucket_name': AWS_BACKUP_STORAGE_BUCKET_NAME,
    'default_acl': 'private',
}
DBBACKUP_CLEAN = False

SLACK_URL = os.environ.get("SLACK_URL", "")
SLACK_TEAM = os.environ.get("SLACK_TEAM", "")
SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")

# Wagtail Birdsong
MJML_EXEC_CMD = './node_modules/.bin/mjml'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "")
REDIS_PORT = os.environ.get("REDIS_PORT", "")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
REDIS_LOCATION = f"{REDIS_URL}/polrev"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Celery
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Reddit
PRAW_CLIENT_ID = os.environ.get("PRAW_CLIENT_ID", "")
PRAW_CLIENT_SECRET = os.environ.get("PRAW_CLIENT_SECRET", "")
PRAW_USERNAME = os.environ.get("PRAW_USERNAME", "")
PRAW_PASSWORD = os.environ.get("PRAW_PASSWORD", "")
