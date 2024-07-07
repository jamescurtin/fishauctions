"""
Django settings for fishauctions project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import sys
import os
try:
    from . import customsettings
except:
    pass
    #print("You can set your envionrment using a customsettings.py file.  No file found, or file is invalid, assuming the environment has been set some other way.")
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ADMINS = [('Admin', os.environ.get('ADMIN_EMAIL', 'admin@example.com'))]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsecure')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DEBUG', '1') == "False":
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['localhost', 'web', '127.0.0.1', '0.0.0.0', os.environ.get('SITE_DOMAIN', ''), os.environ.get('ALLOWED_HOST_1', ''), os.environ.get('ALLOWED_HOST_2', ''), os.environ.get('ALLOWED_HOST_3', '')]
CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://127.0.0.1', 'https://' + os.environ.get('SITE_DOMAIN', ''), 'https://' + os.environ.get('ALLOWED_HOST_1', ''), 'https://' + os.environ.get('ALLOWED_HOST_2', ''), 'https://' + os.environ.get('ALLOWED_HOST_3', '')]

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("redis://:" + os.environ.get('REDIS_PASSWORD', 'unsecure') + "@127.0.0.1:6379/0")],
            #"hosts": [('127.0.0.1', 6379)],
            "capacity": 2000,  # default 100
            "expiry": 20,  # default 60
        },
    },
}

# Application definition
INSTALLED_APPS = [
    'auctions',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    #'site_settings',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_filters',
    'bootstrap_datepicker_plus',
    'el_pagination',
    'easy_thumbnails',
    "post_office",
    'location_field',
    'channels',
    #'debug_toolbar', # having this enabled is handy for sql queries but silences errors in channels
    'markdownfield',
    'qr_code',
    'django_tables2',
    'django_htmx',
    'crispy_bootstrap4',
    'django_recaptcha',
    'chartjs',
]
ASGI_APPLICATION = "fishauctions.asgi.application"
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'fishauctions.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'auctions.context_processors.google_analytics',
                'auctions.context_processors.google_oauth',
                'auctions.context_processors.theme',
                'auctions.context_processors.add_location',
                'auctions.context_processors.dismissed_cookies_tos',
                'auctions.context_processors.add_tz',
            ],
        },
    },
]

WSGI_APPLICATION = 'fishauctions.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TIME_ZONE', 'America/New_York')

USE_I18N = False

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = 'M j, Y P e'

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

SITE_ID = 1
SITE_DOMAIN = os.environ.get('SITE_DOMAIN', '127.0.0.1')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, "staticfiles"))

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Use sqlite for testing
if 'test' in sys.argv:
#if True: # for migrations
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
       
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.mysql'),
            'NAME': os.environ.get('DATABASE_NAME', 'auctions'),
            'USER': os.environ.get('DATABASE_USER', 'mysqluser'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'unsecure'),
            'HOST': os.environ.get('DATABASE_HOST', 'db'),
            'PORT': os.environ.get('DATABASE_PORT', '3306'),
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
#BASE_URL = os.environ.get('BASE_URL', 'http://127.0.0.1:8000')

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login/"
ACCOUNT_FORMS = {
'signup': 'auctions.forms.CustomSignupForm',
'reset_password': 'auctions.forms.CustomResetPasswordForm',
}
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "auction.fish - "
ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
ACCOUNT_CHANGE_EMAIL = True

SESSION_COOKIE_AGE = 1209600*100

EMAIL_BACKEND = 'post_office.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # console
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

POST_OFFICE = {
    'MAX_RETRIES': 4,
    'RETRY_INTERVAL': datetime.timedelta(minutes=15),  # Schedule to be retried 15 minutes later
}

if os.environ.get('EMAIL_USE_TLS', 'True') == "True":
    EMAIL_USE_TLS = True
else:
    EMAIL_USE_TLS = False
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'user@example.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'unsecure')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'user@example.com')
EMAIL_SUBJECT_PREFIX = ""

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY', 'unsecure')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', 'unsecure')

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = False
BOOTSTRAP4 = {
    'include_jquery': True,
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EL_PAGINATION_PER_PAGE = 20
#SITE_URL = os.environ.get('SITE_URL', BASE_URL)

THUMBNAIL_ALIASES = {
    '': {
        'ad': {'size': (250, 150), 'crop': False},
        'lot_list': {'size': (250, 150), 'crop': "smart"},
        'lot_full': {'size': (600, 600), 'crop': False},
    },
}

SECURE_REFERRER_POLICY= "strict-origin-when-cross-origin"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
        'FETCH_USERINFO': True
    }
}
SOCIALACCOUNT_EMAIL_AUTHENTICATION=True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT=True
SOCIALACCOUNT_LOGIN_ON_GET=True

INTERNAL_IPS = [
#    '127.0.0.1', # uncomment this to enable the django debug toolbar
]

VIEW_WEIGHT = 1
BID_WEIGHT = 10
WEIGHT_AGAINST_TOP_INTEREST = 20

GOOGLE_MEASUREMENT_ID=os.environ.get('GOOGLE_MEASUREMENT_ID', 'unsecure')
GOOGLE_TAG_ID = os.environ.get('GOOGLE_TAG_ID', 'unsecure')
GOOGLE_ADSENSE_ID = os.environ.get('GOOGLE_ADSENSE_ID', 'unsecure')

GOOGLE_OAUTH_LINK = os.environ.get('GOOGLE_OAUTH_LINK', 'unsecure')
SECURE_CROSS_ORIGIN_OPENER_POLICY="same-origin-allow-popups"

LOCATION_FIELD_PATH = STATIC_URL + 'location_field'

LOCATION_FIELD = {
    'map.provider': 'google',
    'map.zoom': 13,

    'search.provider': 'google',
    'search.suffix': '',

    # Google
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': os.environ.get('GOOGLE_MAPS_API_KEY', 'unsecure'),
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': (
            LOCATION_FIELD_PATH + '/js/form.js',
        ),
    },
}

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SEND_WELCOME_EMAIL = True # when a user adds an unverified email address to their auction, send an email about the site

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

# the following words are very common and should not be used when generating recommended lots or assigning categories
IGNORE_WORDS = ['albino','red','blue','pair','super','fish','black','breeding','group','fry','female','water','male','trio','green','lot','fin','yellow','gold','large','donation','young','filter','white','fire','blood','and','orange','bag','qty','juvies','starter','adult','hardy','with','small','size','breeders','brown','breeder','pack','two','pink','proven','better','than','more','adults','inch','from','wild','bunch','superb','the','double','reverse','new', 'test']
            