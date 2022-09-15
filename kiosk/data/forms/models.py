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
    title: Title of the question
    question_type: Type of a question (input, textarea, select, checkbox)
"""

INPUT = "I"
TEXTAREA = "T"
SELECT = "S"
CHECKBOX = "C"
QUESTION_TYPE_CHOICES = (
    (INPUT, "Input"),
    (TEXTAREA, "textarea"),
    (SELECT, "Select"),
    (CHECKBOX, "Checkbox"),
)


class FormQuestion(models.Model):
    kiosk_form = models.ForeignKey(
        "forms.KioskForm", on_delete=models.CASCADE, null=False
    )
    title = models.CharField(max_length=64, null=False)
    question_type = models.CharField(
        max_length=1, choices=QUESTION_TYPE_CHOICES, default=INPUT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
What:
    FormAnswer
Attributes:
    kiosk_registration: Registration connected to the answer
    form_question: Question connected to the answer
"""


class FormAnswer(models.Model):
    kiosk_registration = models.ForeignKey(
        "registrations.KioskRegistration", on_delete=models.CASCADE, null=False
    )
    form_question = models.ForeignKey(
        "forms.KioskForm", on_delete=models.CASCADE, null=False
    )
    value = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
