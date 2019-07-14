from dj_database_url import parse

from decouple import config

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': config('DATABASE_URL', cast=parse)
}

DEBUG = False

SECRET_KEY = config('SECRET_KEY', cast=str)

