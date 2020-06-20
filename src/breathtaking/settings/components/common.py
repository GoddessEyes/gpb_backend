"""Общие настройки django-app."""

import os


AUTH_USER_MODEL = 'eauth.User'

ACCOUNT_EMAIL_VERIFICATION = 'none'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'corsheaders',
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'mptt',
    'ckeditor',
)

LOCAL_APPS = (
    'breathtaking.modules.eauth',
    'breathtaking.modules.department_tree',
    'breathtaking.modules.ideas',
    'breathtaking.modules.solutions',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6_s9k)_72_rqh7p@5je_ehapg9gbtm3u4frkcu73-^)@8!sm32'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 1024,
        'width': 1024,
    },
}
