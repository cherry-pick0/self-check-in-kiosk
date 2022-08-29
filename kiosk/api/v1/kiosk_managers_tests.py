from api.utils.kiosk_scenarios import KioskScenario
from rest_framework.test import APITransactionTestCase


class KioskManagersTests(APITransactionTestCase):
    def setUp(self) -> None:
        self.scenario = KioskScenario()
        self.scenario = self.scenario.add_admin()

    def test_add_kiosk_manager(self):
        pass
