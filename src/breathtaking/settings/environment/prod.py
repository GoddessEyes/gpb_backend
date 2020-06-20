"""Окружение для прод-стенда."""
from corsheaders.defaults import default_headers, default_methods

from breathtaking.settings.environment.base import *


ALLOWED_HOSTS = ('*', )

CORS_ORIGIN_ALLOW_ALL = False

DEBUG = False
