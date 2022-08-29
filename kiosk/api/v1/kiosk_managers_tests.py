from api.utils.kiosk_scenarios import KioskScenario
from rest_framework import status
from rest_framework.test import APITestCase


class KioskManagersTests(APITestCase):
    def setUp(self) -> None:
        self.scenario = KioskScenario(self)
        self.scenario = self.scenario.add_admin()

    def test_add_kiosk_manager(self):
        # Admin logs in
        self.client.login(token=self.scenario.admin_token)

        # Admin creates a kiosk manager
        manager_data = {}
        response = self.client.post(
            "/api/v1/kiosk-managers", manager_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
