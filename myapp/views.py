import datetime
import logging

from djeasyview.views import DjeasyListCreateAPI, DjeasyRetrieveUpdateAPI
from rest_framework.permissions import AllowAny

from django.shortcuts import render

from .models import User
from .serializers import UserSerializer

logger = logging.getLogger(__name__)


def index(request):
    logger.warning(
        "Homepage was accessed at " + str(datetime.datetime.now()) + " hours!"
    )
    return render(request, "index.html")


def page1(request):
    return render(request, "page1.html")


def docs(request):
    return render(request, "site/index.html")


class UserListCreateApiView(DjeasyListCreateAPI):
    model = User
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    list_serializer_class = UserSerializer
    create_serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPiview(DjeasyRetrieveUpdateAPI):
    model = User
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    update_serializer_class = UserSerializer
    retrieve_serializer_class = UserSerializer

    def dispatch(self, request, *args, **kwargs):
        self.context = {"user": self.request.user.id}
        return super().dispatch(request, *args, **kwargs)
