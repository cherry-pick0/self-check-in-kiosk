from api.utils.kiosk_scenarios import KioskScenario
from rest_framework import status
from rest_framework.test import APITransactionTestCase


class KioskUsersTests(APITransactionTestCase):
    def setUp(self) -> None:
        self.scenario = KioskScenario(self)
        self.scenario = self.scenario.add_admin()

    def test_add_kiosk_user(self):
        # Admin logs in
        self.scenario.login(self.scenario.admin_token)

        # Admin creates a kiosk user
        kiosk_user_data = {
            "email": "user@kiosk.com",
            "first_name": "",
            "last_name": "",
        }
        response = self.client.post(
            "/api/v1/kiosk-users",
            kiosk_user_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(kiosk_user_data, response.data)
