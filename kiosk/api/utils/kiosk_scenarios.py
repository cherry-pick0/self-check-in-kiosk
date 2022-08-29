from data.users.models import KioskUser
from rest_framework.test import APITransactionTestCase

"""
Create scenarios for api tests.
"""


class KioskScenario(APITransactionTestCase):
    admin_user: KioskUser = None

    def add_admin(self):
        # Use direct db, if api isn't available
        email = "admin@kiosk.com"
        admin_user, _ = KioskUser.objects.get_or_create(email=email, is_staff=True)
        self.admin_user = admin_user

        return self
