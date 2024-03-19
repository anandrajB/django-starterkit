import os
from pathlib import Path

import dotenv

# --------------#
#  ENV CONFIG   #
# --------------#


BASE_DIR = Path(__file__).resolve().parent.parent


dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


# -----------------------#
#  IMPORTANT CONFIG - 1  #
# -----------------------#

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",
    "rest_framework",
    "rest_framework.authtoken",
]


ROOT_URLCONF = "myproject.urls"


# ------------------#
#  TEMPLATE CONFIG  #
# ------------------#


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# -----------------------#
#  IMPORTANT CONFIG - 2  #
# -----------------------#


WSGI_APPLICATION = "myproject.wsgi.application"


# -------------------#
#  DATABASE CONFIG   #
# -------------------#

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "mydatabase"),
        "USER": os.environ.get("POSTGRES_USER", "myuser"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "mypassword"),
        "HOST": "postgres",
        "PORT": "5432",
    }
}


# ---------------------#
#     AUTHENTICATION   #
# ---------------------#

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "myproject.authentication.CustomAuthenticationBackend",
]


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ---------------#
#  AUTH SETUP    #
# ---------------#

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",
    ],
}


# ---------------#
#  EMAIL SETUP   #
# ---------------#


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "example@host.com"
EMAIL_HOST_PASSWORD = "mypassword"


# -----------------------#
#  CELERY CONFIGURATION  #
# -----------------------#

CELERY_BROKER_URL = os.environ.get("CELERY_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_URL")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TIMEZONE = "Asia/Kolkata"


# -----------------------#
#  INTERNATIONALIZATION   #
# -----------------------#


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# -------------------------#
#  STATIC AND MEDIA CONFIG  #
# --------------------------#

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# --------------------#
#  MIDDLEWARE CONFIG  #
# --------------------#


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# -----------------#
#  LOGGING CONFIG  #
# ----------------#


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}


# -----------------#
#  SENTRY CONFIG  #
# ----------------#


# import sentry_sdk
# from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
# from sentry_sdk.integrations.django import DjangoIntegration


# sentry_sdk.init(
#     dsn="https://mysentrydsn.com",
#     integrations=[
#         DjangoIntegration(),
#     ],
#     # in_production
#     profiles_sample_rate=1.0,
#     traces_sample_rate=1.0,
#     sample_rate=0.25,
#     send_default_pii=True,
# )
