from .base import *  # noqa

# ------------------------#
#  BASE CONFIGURATION      #
# ------------------------#

DEBUG = False

DEV = False

ALLOWED_HOSTS = ["*"]


# --------------------#
#  CSRF SETTINGS      #
# --------------------#

CSRF_TRUSTED_ORIGINS = ["*"]

CSRF_COOKIE_SECURE = True

CSRF_FAILURE_VIEW = "myapp.views.csrf_failure"
