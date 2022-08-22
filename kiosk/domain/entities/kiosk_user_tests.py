from unittest import TestCase

from kiosk.domain.entities.kiosk_user import KioskUser


class KioskUserTests(TestCase):
    def test_kiosk_user(self):
        kiosk_user = KioskUser(0)
        self.assertEqual(kiosk_user.entity_id, 0)
