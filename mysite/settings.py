"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

print BASE_DIR
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ng5vb(2ufvu4&nj-4pjoig%8k3+xpu4%l*n@m1r3ip*p@)q8i1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, '../templates'),)

FIXTURE_DIRS = (os.path.join(PROJECT_PATH, '../fixtures'),)

MEDIA_ROOT = os.path.join(PROJECT_PATH, '/var/www/html/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),)

MEDIA_URL = '/var/www/html/'

VAR = 0

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'ws4redis.context_processors.default',
)

# List of callables that know how to import templates from various sources.


SESSION_ENGINE = 'redis_sessions.session' # for djcelery

SESSION_REDIS_PREFIX = 'session'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ticket',
    'monitoreo',
    'ws4redis',
    'corsheaders',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)



ROOT_URLCONF = 'mysite.urls'

# This setting is required to override the Django's main loop, when running in
# development mode, such as ./manage runserver
WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# URL that distinguishes websocket connections from normal requests
WEBSOCKET_URL = '/ws/'

# Set the number of seconds each message shall persited
WS4REDIS_EXPIRE = 3600

WS4REDIS_HEARTBEAT = '--heartbeat--'

WS4REDIS_PREFIX = 'demo'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'tasky',
        'USER': 'root',
        'PASSWORD': 'd4t4B4$3*',
        'HOST': '188.166.72.64',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/



STATIC_URL = '/static/'

'''
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@sandboxbb5414fe26d94969aa76e2ece53f668e.mailgun.org'
EMAIL_HOST_PASSWORD = '5d72732e427556dbec56cbaf89ce5836'
EMAIL_PORT = 587


'''
CORS_ORIGIN_ALLOW_ALL = True

EMAIL_HOST = 'mail.xiencias.org'
EMAIL_HOST_USER = 'andyjo@xiencias.org'
EMAIL_HOST_PASSWORD = '02190144'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
