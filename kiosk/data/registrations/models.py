from django.db import models

"""
Attributes:
    unique_identifier: Reference by which registration/guest can be distinguished
    kiosk: Kiosk can have many Registrations
    kiosk_user: Registration on Kiosk can be linked to an existing User
"""


class KioskRegistration(models.Model):
    unique_identifier = models.CharField(max_length=256, unique=True)
    kiosk_user = models.ForeignKey(
        "users.KioskUser", on_delete=models.SET_NULL, null=True
    )
    kiosk = models.ForeignKey("kiosks.Kiosk", on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "kiosk",
            "kiosk_user",
        )
