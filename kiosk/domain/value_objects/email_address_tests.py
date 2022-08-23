from unittest import TestCase

from kiosk.domain.value_objects.email_address import EmailAddress, EmailInvalidException


class EmailAddressTests(TestCase):
    def test_email_address(self):
        email = "test@kiosk.com"
        email_address = EmailAddress(email)
        self.assertEqual(email_address.email, email)

    def test_email_address_invalid_email(self):
        with self.assertRaises(EmailInvalidException):
            EmailAddress("")
