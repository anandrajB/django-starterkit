from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from myapp.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path(f"v{settings.APP_VERSION}/", include("myproject.urls.routes")),
]
