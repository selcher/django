__author__ = 'SAMSUNG'

from .base import *


DEBUG = True

# TODO: use environment variables pattern
SECRET_KEY = 'h3ll0Sh00t1ngSt4r'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# INSTALLED_APPS += ('debug_toolbar', )
