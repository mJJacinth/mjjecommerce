import django_on_heroku
from decouple import fashionfreak
from .base import *

SECRET_KEY = fashionfreak('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'Fashion-basic-fashionfreak.herokuapp.com',
    'fashion.blog',
]