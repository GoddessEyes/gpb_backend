from corsheaders.defaults import default_headers, default_methods

from breathtaking.settings.environment.base import *


ALLOWED_HOSTS = ('*', )

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ALLOW_CREDENTIALS = False

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = list(default_headers)

CORS_ALLOW_METHODS = list(default_methods)

DEBUG = True
