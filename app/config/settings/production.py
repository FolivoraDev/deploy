from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

DATABASES = secrets['DATABASES']

