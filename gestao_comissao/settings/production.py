import dj_database_url
from dj_database_url import parse as db_url

from decouple import config

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

DEBUG = False

SECRET_KEY = config('SECRET_KEY', cast=str)

