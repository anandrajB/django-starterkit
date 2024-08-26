from django.conf.urls import include
from django.urls import path
from django.urls.conf import include


# ------------------------------------------------------------------------------------------

# BASE URL FOR ACCOUNTS

# -------------------------------------------------------------------------------------------


urlpatterns = [
    path("user/", include("myapp.path.user"), name="user details"),
]
