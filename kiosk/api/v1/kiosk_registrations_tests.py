from api.utils.kiosk_scenarios import KioskScenario
from rest_framework.test import APITransactionTestCase


class KioskRegistrationsTests(APITransactionTestCase):
    def setUp(self) -> None:
        self.scenario = KioskScenario(self)
        self.scenario = self.scenario.add_admin()

    def test_kiosk_registration(self):
        self.scenario = self.scenario.add_kiosk_user()
        # Create Kiosk Manager
        # Create Kiosk as a Kiosk Manager
        # Add questions to the Kiosk Form

        # Unauthenticated user fetches the Kiosk form

        # Unauthenticated user is trying to register
        # as a guest and create a user account

        # As an Unregistered User I can confirm my email address,
        # in order to validate my identity.

        # As an Unregistered User I can login to the platform,
        # in order to see the Kiosk Manager platform.

    def test_kiosk_registration_no_auth(self):
        pass
        # Unauthenticated user is trying to register as a guest.
        # Similar as above.
