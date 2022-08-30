from django.db import models


class KioskGuestObjects(models.Manager):
    pass


"""
What:
    A model used to represent a Guest

Attributes:
    unique_identifier: Reference by which guest can be distinguished
    kiosk_user: Guest can create a user account
"""


class KioskGuest(models.Model):
    unique_identifier = models.CharField(max_length=256, unique=True)
    kiosk_user = models.OneToOneField(
        "users.KioskUser", on_delete=models.SET_NULL, unique=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = KioskGuestObjects()
