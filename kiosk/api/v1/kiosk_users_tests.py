from api.utils.kiosk_scenarios import KioskScenario
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from kiosk.celery import send_emails


class KioskUsersTests(APITransactionTestCase):
    def setUp(self) -> None:
        self.scenario = KioskScenario(self)
        self.scenario = self.scenario.add_admin()

    @override_settings(SEND_EMAILS=True)
    def test_add_kiosk_user(self):
        # Admin logs in
        self.scenario.login(self.scenario.admin_token)

        # Admin creates a kiosk user
        email = "user@kiosk.com"
        kiosk_user_data = {
            "email": email,
            "first_name": "",
            "last_name": "",
        }
        response = self.client.post(
            "/api/v1/kiosk-users",
            kiosk_user_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        kiosk_user_data["id"] = response.data.get("id")
        self.assertEqual(kiosk_user_data, response.data)

        # TODO Emails must be sent to queue

        # We don't have api for emails, so check directly in db
        from data.emails.models import DataModelEmail

        self.assertEqual(
            DataModelEmail.objects.filter(
                receiver_email=email, status=DataModelEmail.QUEUE
            ).count(),
            1,
        )

        # Only for testing
        send_emails.run()

        self.assertEqual(
            DataModelEmail.objects.filter(
                receiver_email=email, status=DataModelEmail.SENT
            ).count(),
            1,
        )
