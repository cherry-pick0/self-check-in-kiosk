from unittest import TestCase

from kiosk.domain.entities.kiosk_user import KioskUser
from kiosk.domain.services.add_kiosk_user import (
    AddKioskUserIParams,
    AddKioskUserUsersIRepository,
    ServiceAddKioskUser,
)
from kiosk.domain.value_objects.email_address import EmailAddress


class AddKioskUserTestsUsersRepository(AddKioskUserUsersIRepository):
    def add(self, kiosk_user: KioskUser) -> KioskUser:
        return kiosk_user


class AddKioskUserTestsParams(AddKioskUserIParams):
    _kiosk_user: KioskUser = None

    @property
    def kiosk_user(self) -> KioskUser:
        return self._kiosk_user


class ServiceAddKioskUserTests(TestCase):
    def test_add_kiosk_user(self):
        # Add a new KioskUser
        email = "test@kiosk.com"
        name = "Test"
        params = AddKioskUserTestsParams()
        params._kiosk_user = KioskUser(0, EmailAddress(email), name)
        users = AddKioskUserTestsUsersRepository()

        service = ServiceAddKioskUser()
        service.users = users
        service.execute(params)

        # Email address and name are the one chosen on creation
        self.assertEqual(service.kiosk_user.email_address.email, email)
        self.assertEqual(service.kiosk_user.name, name)
