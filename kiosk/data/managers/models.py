from django.db import models


class KioskManagerObjects(models.Manager):
    pass


"""
What:
    A model used to represent a Manager, who can create his own Kiosks

Attributes:
    kiosk_user: Manager needs to have a user account
"""


class KioskManager(models.Model):
    kiosk_user = models.OneToOneField(
        "users.KioskUser", on_delete=models.CASCADE, unique=True, null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = KioskManagerObjects()
