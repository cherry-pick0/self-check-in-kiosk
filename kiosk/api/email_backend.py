from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

"""
Django's default authentication works on username and password fields.
Email authentication backend will authenticate users based on email and password.

https://riptutorial.com/django/example/4212/email-authentication-backend
"""


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        return None
