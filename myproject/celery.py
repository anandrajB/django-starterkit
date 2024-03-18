import os

from celery import Celery

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")


app.conf.broker_url = os.environ.get("CELERY_URL")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
