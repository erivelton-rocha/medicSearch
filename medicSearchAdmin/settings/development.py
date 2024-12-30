from .settings import *
import os

DEBUG = True

SECRET_KEY = 'kw9=nxdpk#$k1g^@%htnw3w00bpic4-myqh_#*fn2-qdi(vl7m'

# Você também pode deixar em branco com colchetes vazios []
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}