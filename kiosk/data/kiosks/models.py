from django.db import models

"""
Attributes:
    kiosk_manager: Manager can have many kiosks
    kiosk_form: One kiosk has one Form
"""


class Kiosk(models.Model):
    kiosk_manager = models.ForeignKey(
        "managers.KioskManager", on_delete=models.CASCADE, null=False
    )
    kiosk_form = models.OneToOneField(
        "forms.KioskForm", on_delete=models.PROTECT, unique=True, null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
