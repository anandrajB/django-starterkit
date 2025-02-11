from rest_framework.serializers import ModelSerializer

from myapp.models import User, Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
