from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from myapp.views import (
    docs,
    index,
    page1,
)

# ------------------------------------------------------------------------------------------

# URLS FOR USER , OTP SENDING , OTP VERIFY

# -------------------------------------------------------------------------------------------


urlpatterns = [
    path("user/", include("myapp.urls")),
    path("page1", page1, name="page-1"),
    path("docs/", docs, name="documentation"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
