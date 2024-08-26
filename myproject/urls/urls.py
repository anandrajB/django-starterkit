from django.contrib import admin
from django.urls import path, include
from myapp.views import (
    docs,
    index,
    page1,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("user/", include("myapp.urls")),
    path("page1", page1, name="page-1"),
    path("docs/", docs, name="documentation"),
]
