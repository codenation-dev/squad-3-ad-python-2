from decouple import config

ALLOWED_HOSTS = ['*']

DEBUG = False

SECRET_KEY = config('SECRET_KEY', cast=str)

