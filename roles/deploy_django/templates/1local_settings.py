import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'k!1oc&ld=fr0(=j_77(+omi=s+_pk-%dk0$vs8c9nl85-n-zgy'

DEBUG = false

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'djrest.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-rest-db',
        'USER': 'ubuntu',
        'PASSWORD': 'ubuntu',
        # 'HOTS': '',
        # 'POST': ''
    }
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
