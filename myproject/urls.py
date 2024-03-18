from django.contrib import admin
from django.urls import path
from myapp.views import (
    UserListCreateApiView,
    UserRetrieveUpdateDestroyAPiview,
    docs,
    index,
    page1,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("user/", UserListCreateApiView.as_view(), name="user-list-create-api"),
    path(
        "user/<int:pk>/",
        UserRetrieveUpdateDestroyAPiview.as_view(),
        name="user-retrieve-update-api",
    ),
    path("page1", page1, name="page-1"),
    path("docs/", docs, name="documentation"),
]
