import os
from pathlib import Path
from myproject.database.connection import DATABASE_CONFIG
import os
import dotenv

# --------------#
#  ENV CONFIG   #
# --------------#


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ALLOWED_HOSTS = ["*"]

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


# -----------------------#
#  IMPORTANT CONFIG - 1  #
# -----------------------#

SECRET_KEY = os.environ.get("SECRET_KEY")


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


ROOT_URLCONF = "myproject.urls.urls"


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


WSGI_APPLICATION = "myproject.server.wsgi.application"
ASGI_APPLICATION = "myproject.server.wsgi.application"

# -------------------#
#  DATABASE CONFIG   #
# -------------------#

DATABASES = DATABASE_CONFIG


# ---------------------#
#     AUTHENTICATION   #
# ---------------------#

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "myproject.config.authentication.CustomAuthenticationBackend",
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
