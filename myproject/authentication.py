from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from typing import Optional

User = get_user_model()


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(
        self, request, email: Optional[str] = None, password: Optional[str] = None
    ):
        try:
            """write your own custom logic"""
            pass
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
