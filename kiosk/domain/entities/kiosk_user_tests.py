from unittest import TestCase

from domain.entities.kiosk_user import KioskUser
from domain.value_objects.email_address import EmailAddress


class KioskUserTests(TestCase):
    def test_kiosk_user(self):
        email_address = EmailAddress("user@kiosk.com")
        kiosk_user = KioskUser(email_address, entity_id_value=0)
        self.assertEqual(kiosk_user.entity_id, 0)

    def test_kiosk_user_name(self):
        email_address = EmailAddress("user@kiosk.com")
        first_name = "John"
        last_name = "Doe"
        kiosk_user = KioskUser(email_address, first_name, last_name, entity_id_value=0)
        self.assertEqual(kiosk_user.entity_id, 0)
        self.assertEqual(kiosk_user.first_name, first_name)
        self.assertEqual(kiosk_user.last_name, last_name)
        self.assertEqual(kiosk_user.name, f"{first_name} {last_name}")
