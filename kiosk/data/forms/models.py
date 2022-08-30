from django.db import models

"""
What:
    KioskForm
Attributes:
    kiosk: One kiosk can have one form
"""


class KioskForm(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
What:
    FormQuestion
Attributes:
    kiosk_form: One form can have multiple questions
"""


class FormQuestion(models.Model):
    kiosk_form = models.ForeignKey(
        "forms.KioskForm", on_delete=models.CASCADE, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
