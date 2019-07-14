from decouple import config

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': config('DATABASE_URL')
}

DEBUG = False

SECRET_KEY = config('SECRET_KEY', cast=str)

