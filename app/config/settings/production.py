from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.prod.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

DATABASES = secrets['DATABASES']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filename': os.path.join(ROOT_DIR, '.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
