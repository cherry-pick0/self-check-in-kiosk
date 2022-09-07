from unittest import TestCase

from domain.entities.email import Email
from domain.value_objects.email_address import EmailAddress


class EmailTests(TestCase):
    def test_email(self):
        email_address = EmailAddress("user@kiosk.com")
        name = "name"
        subject = "subject"
        body = "body"
        status = "status"

        email = Email(email_address, name, subject, body, status, entity_id_value=0)
        self.assertEqual(email.entity_id, 0)
        self.assertEqual(email.email_address.email, email_address.email)
        self.assertEqual(email.name, name)
        self.assertEqual(email.subject, subject)
        self.assertEqual(email.body, body)
        self.assertEqual(email.status, status)
