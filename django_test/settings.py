"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import django_heroku
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+d@m_8gzm-bu46)srp$xpk8_y&#-x^g!yrqhab(r$n#8h19a0!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django-test-inso.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index.apps.IndexConfig',
    'rest_framework',
    'register.apps.RegisterConfig',
    "crispy_forms",
    'social_django'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django_session_timeout.middleware.SessionTimeoutMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_test.wsgi.application'

# Databases
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {

    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'testing_db',
        'USER' : 'psqlMaster',
        'PASSWORD' : 'psqlmasterpassword',
        'HOST' : 'backlog-handler-db.cobkfpis7wr9.us-east-2.rds.amazonaws.com',
        'PORT' : '5000'
    },

    'production' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'production_db',
        'USER' : 'psqlMaster',
        'PASSWORD' : 'psqlmasterpassword',
        'HOST' : 'backlog-handler-db.cobkfpis7wr9.us-east-2.rds.amazonaws.com',
        'PORT' : '5000'
    }

}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Activate Django-Heroku.
django_heroku.settings(locals())

CRISPY_TEMPLATE_PACK = "bootstrap4"


SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_GITHUB_KEY = "dc717cb689d0bd2f2348"
SOCIAL_AUTH_GITHUB_SECRET = "766e44c6c703203b4e12c351f4b954758a66f246"

SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SESSION_EXPIRE_SECONDS = 120
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60
SESSION_TIMEOUT_REDIRECT = '/'


