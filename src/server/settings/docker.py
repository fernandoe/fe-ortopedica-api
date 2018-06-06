from .base import *

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}
