"""Модуль конфигурации Базы Данных."""

import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'gpb_postgres'),
        'USER': os.getenv('POSTGRES_USER', 'gpb_postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'gpb_postgres'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}
