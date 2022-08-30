from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class KioskUserObjects(UserManager):
    pass


"""
What:
    A model used to represent a KioskUser account.
    Part of user authentication system.
    Extending AbstractBaseUser, which allows us more customizations.

Attributes:
    is_active: if not active, the account is restricted from any actions
    is_staff: specifies if KioskUser is an admin
"""


class KioskUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Auth with email
    USERNAME_FIELD = "email"

    objects = KioskUserObjects()
