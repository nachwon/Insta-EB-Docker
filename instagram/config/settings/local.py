import logging
import random
import string

from .base import *

logger = logging.getLogger('__name__')

ALLOWED_HOSTS = [
    # 'localhost',
    # '127.0.0.1',
    '.elasticbeanstalk.com',
]

logger.debug(str(ALLOWED_HOSTS))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''.join([random.choice(string.ascii_lowercase) for i in range(40)])

DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'class': 'logging.StreamHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(ROOT_DIR, '.log', 'django.log')
        },

    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
                'file',
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


