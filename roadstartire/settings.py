"""
Django settings for roadstartire project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True

import os
import environ

environ.Env()
environ.Env.read_env()


import environ
environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hc=@aet_2rzy+54#hnyoz)nco%fq@s8#^s%u67!z4pflgi=zdl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG_VALUE'] == 'True'

ALLOWED_HOSTS = [
    '*',
    'localhost',
    '127.0.0.1',
    'www.roadstartirewholesale.ca',
    'road-star.herokuapp.com',
]

# Application definition

INSTALLED_APPS = [
    'timezone_field',
    'main_app',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'roadstartire.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'roadstartire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'roadstartire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'roadstar',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

email_key = os.environ['EMAIL']
password_key = os.environ['PASSWORD']

#required to send email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = email_key
EMAIL_HOST_PASSWORD = password_key
EMAIL_PORT = 587
ADMINS = [('Mohsen', email_key)]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Need this so that Django knows to use the new User class
AUTH_USER_MODEL = 'users.CustomUser'

# The absolute path to the directory where collectstatic will collect static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'main_app/static'),
)

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

# ────────────────────────────────────────────────────────────────────────────────

# Custom code to sort the Admin Index page

# Ordering list
# ADMIN_ORDERING = [
#     ('users', [
#         'CustomUser',
#     ]),
#     ('main_app', [
#         'Tire',
#         'Cart',
#         'CartDetail',
#     ]),

# ]
# # Sort function
# def get_app_list(self, request):
#     app_dict = self._build_app_dict(request)
#     for app_name, object_list in ADMIN_ORDERING:
#         app = app_dict[app_name]
#         app['models'].sort(key=lambda x: object_list.index(x['object_name']))
#         yield app

# # Cover the django.contrib.admin.AdminSite.get_app_list
# from django.contrib import admin

# admin.AdminSite.get_app_list = get_app_list
