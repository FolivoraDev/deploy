from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

DATABASES = secrets['DATABASES']
