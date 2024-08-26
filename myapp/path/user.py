from django.contrib import admin
from django.urls import path
from myapp.api.user import (
    UserListCreateApiView,
    UserRetrieveUpdateDestroyAPiview,
)

urlpatterns = [
    path("", UserListCreateApiView.as_view(), name="user-list-create-api"),
    path(
        "<int:pk>/",
        UserRetrieveUpdateDestroyAPiview.as_view(),
        name="user-list-create-api",
    ),
]
