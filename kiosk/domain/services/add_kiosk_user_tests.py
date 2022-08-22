# As an Unregistered User I can create a Manager account,
# in order to access Manager features.
from unittest import TestCase

from kiosk.domain.services.add_kiosk_user import ServiceAddKioskUser


class ServiceAddKioskUserTests(TestCase):
    def add_kiosk_user_test(self):
        # Add a new KioskUser
        service = ServiceAddKioskUser()
        kiosk_user = service.execute()

        # Email address and name are the one chosen on creation
        self.assertEqual(kiosk_user.email, "")

    def add_kiosk_manager(self):
        pass
        # Add a new KioskUser
        # Add a new KioskManager, connected to the new KioskUser
