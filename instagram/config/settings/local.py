import random
import string

from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'http://che1.ap-northeast-2.elasticbeanstalk.com/',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''.join([random.choice(string.ascii_lowercase) for i in range(40)])

