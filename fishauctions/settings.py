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
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ['DEBUG'] == "True":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', os.environ['ALLOWED_HOSTS']]

# Application definition

INSTALLED_APPS = [
    'auctions',
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
    'django_filters',
    'bootstrap_datepicker_plus',
    'el_pagination',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
            ],
        },
    },
]

WSGI_APPLICATION = 'fishauctions.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ['TIME_ZONE']

USE_I18N = True

USE_L10N = True

USE_TZ = True

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
SITE_DOMAIN = os.environ['SITE_DOMAIN']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

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
            'ENGINE': os.environ['DATABASE_ENGINE'],
            'NAME': os.environ['DATABASE_NAME'],
            'USER': os.environ['DATABASE_USER'],
            'PASSWORD': os.environ['DATABASE_PASSWORD'],
            'HOST': os.environ['DATABASE_HOST'],
            'PORT': os.environ['DATABASE_PORT'],
        }
    }

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.environ['BASE_URL']

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login/"
ACCOUNT_FORMS = {
'signup': 'auctions.forms.CustomSignupForm',
}
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "TFCB - "

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # console
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

if os.environ['EMAIL_USE_TLS'] == "True":
    EMAIL_USE_TLS = True
else:
    EMAIL_USE_TLS = False
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_SUBJECT_PREFIX = ""

CRISPY_TEMPLATE_PACK = 'bootstrap4'
BOOTSTRAP4 = {
    'include_jquery': True,
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EL_PAGINATION_PER_PAGE = 40