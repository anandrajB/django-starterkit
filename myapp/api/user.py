
from djeasyview.views import DjeasyListCreateAPI, DjeasyRetrieveUpdateAPI
from rest_framework.permissions import AllowAny


from myapp.models import User
from myapp.serializers.user import UserSerializer


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
