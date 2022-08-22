from unittest import TestCase

from kiosk.domain.entities.kiosk_user import KioskUser
from kiosk.domain.value_objects.email_address import EmailAddress


class KioskUserTests(TestCase):
    def test_kiosk_user(self):
        email_address = EmailAddress("")
        kiosk_user = KioskUser(0, email_address)
        self.assertEqual(kiosk_user.entity_id, 0)
