from decouple import config

ALLOWED_HOSTS = ['*']

SECRET_KEY = config('SECRET_KEY', cast=str)

