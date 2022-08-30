from data.users.models import KioskUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITransactionTestCase

"""
Create scenarios for api tests.
"""


class KioskScenario:
    admin_user: KioskUser = None
    kiosk_user_id: int = None
    admin_token = None
    _test_case = None

    def __init__(self, test_case: APITransactionTestCase):
        if not isinstance(test_case, APITransactionTestCase):
            raise TypeError("Invalid test_case")

        self._test_case = test_case

    def login(self, token):
        self._test_case.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

    def logout(self):
        self._test_case.client.credentials()

    def add_admin(self):
        # Use direct db, if api isn't available
        email = "admin@kiosk.com"
        password = "password"
        password_hash = make_password(password)
        admin_user, _ = KioskUser.objects.get_or_create(
            email=email, is_staff=True, password=password_hash
        )
        self.admin_user = admin_user

        # todo Authentication flow
        self.admin_token, _ = Token.objects.get_or_create(user=self.admin_user)

        login_data = {"username": email, "password": password}
        response = self._test_case.client.post(
            "/api/token-auth", login_data, format="json"
        )
        self._test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        self.admin_token = response.data.get("token")

        return self

    def add_kiosk_user(self):
        # Admin logs in
        self.login(self.admin_token)

        # Admin creates a kiosk user
        kiosk_user_data = {
            "email": "user@kiosk.com",
            "first_name": "",
            "last_name": "",
        }
        response = self._test_case.client.post(
            "/api/v1/kiosk-users",
            kiosk_user_data,
            format="json",
        )
        self._test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.kiosk_user_id = response.data.pop("id")
        self._test_case.assertEqual(kiosk_user_data, response.data)
        self.logout()

        return self
