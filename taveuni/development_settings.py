import os

from taveuni.settings import REST_FRAMEWORK, START_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s][%(name)s:%(lineno)s][%(levelname)s] %(message)s',
            'datefmt': '%Y/%b/%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'qinspect': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
__app_logging = {
    'handlers': ['console', ],
    'level': 'DEBUG',
    'propagate': True
}
for proj_app in START_APPS:
    LOGGING.get('loggers').update({proj_app: __app_logging})

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
        'anon': '10000/min'  # set this as large as possible in development
    }


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
LATEST_RESULTS_KEY = os.environ.get('LATEST_RESULTS_KEY',
                                    'we-cannot-get-latest-results-key')

CAPTCHA_TEST_MODE = True

RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
RABBITMQ_DEFAULT_VHOST = os.environ.get('RABBITMQ_DEFAULT_VHOST')
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'taveuni-rabbitmq')
BROKER_URL = (f'amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}'
              f'@{RABBITMQ_HOST}:5672/{RABBITMQ_DEFAULT_VHOST}')
# Needed to seperate the broker sending a produce message
# to be able to publish task on the correct broker
BROKER_WRITE_URL = BROKER_URL  # to set a specific broker value
# `BROKER_READ_URL` meanwhile, its default value of `BROKER_READ_URL` is the BROKER_URL defined
ASK_RESULTS_BROKER_URL = os.environ.get('ASK_RESULTS_BROKER_URL', BROKER_WRITE_URL)


REDIS_HOST = os.environ.get('REDIS_HOST', 'taveuni-redis')
REDIS_CACHE_LOCATION = f'redis://{REDIS_HOST}:6379'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if os.environ.get('DOCKERIZED'):  # To avoid error in makemigrations during build
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': os.environ.get('POSTGRES_SERVICE'),
            'NAME': os.environ.get('POSTGRES_DB'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'PORT': os.environ.get('POSTGRES_PORT'),
            'USER': os.environ.get('POSTGRES_USER')
        }
    }

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': REDIS_CACHE_LOCATION,
        'OPTIONS': {
            'DB': 1,
        }
    },
}

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 0))
EMAIL_USE_TLS = True
DEFAULT_TO_EMAIL = os.environ.get('DEFAULT_TO_EMAIL', '').split(',')
EMAIL_CLIENT_ERRORS = os.environ.get('EMAIL_CLIENT_ERRORS',
                                     'notifier@unnotech.com').split(',')
