from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class KioskUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, help_text="Is this user admin?")

    # Auth with email
    USERNAME_FIELD = "email"
