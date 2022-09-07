from django.db import models

"""
What:
    DataModelEmail
Attributes:
    receiver_name: Name of a receiver
    receiver_email: Email address
    subject: Email subject
    body: Email body
    status: Helps dealing with emails based on status
    error_message: Possible errors when creating/sending
"""

CREATED = "C"
QUEUE = "Q"
SENT = "S"
ERROR = "E"
EMAIL_STATUS_CHOICES = (
    (CREATED, "Created"),
    (QUEUE, "Queue"),
    (SENT, "Sent"),
    (ERROR, "Error"),
)


class DataModelEmail(models.Model):
    receiver_email = models.EmailField(max_length=256)
    receiver_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=50)
    body = models.TextField()
    status = models.CharField(
        max_length=1, choices=EMAIL_STATUS_CHOICES, default=CREATED
    )
    error_message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
