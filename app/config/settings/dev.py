from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

DATABASES = secrets['DATABASES']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

LOG_DIR = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'handlers': {
        'file_error': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filename': os.path.join(LOG_DIR, '.log'),
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file_error', 'console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

DEBUG = False
ALLOWED_HOSTS = ['abc']
