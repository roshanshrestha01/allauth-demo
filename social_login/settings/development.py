import os

from social_login.settings import BASE_DIR, TEMPLATES, INSTALLED_APPS, MIDDLEWARE

SECRET_KEY = '_n8_1vxfksbwy0$vwqdc%^4_2kg0n0^jd0363i47i*$rhs0c4n'

DEBUG = True

ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = '127.0.0.1'

