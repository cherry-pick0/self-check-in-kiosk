from unittest import TestCase

from domain.domain_events.factory import IDomainEventsRunner
from domain.entities.kiosk_user import KioskUser
from domain.services.add_kiosk_user import (
    AddKioskUserParams,
    AddKioskUserUsersIRepository,
    ServiceAddKioskUser,
)


class FakeDomainEventRunner(IDomainEventsRunner):
    def trigger(self, *_, **__):
        pass


class AddKioskUserTestsUsersRepository(AddKioskUserUsersIRepository):
    __kiosk_user = None

    def add(self, kiosk_user: KioskUser):
        self.__kiosk_user = kiosk_user
        return kiosk_user

    def get_by_id(self, kiosk_user_id: int) -> KioskUser:
        return self.__kiosk_user


class ServiceAddKioskUserTests(TestCase):
    def test_add_kiosk_user(self):
        # Add a new KioskUser
        email = "test@kiosk.com"
        first_name = "Test"
        data = {"email": email, "first_name": first_name}
        params = AddKioskUserParams(data)
        kiosk_users = AddKioskUserTestsUsersRepository()

        service = ServiceAddKioskUser()
        service.domain_event_runner = FakeDomainEventRunner()
        service.kiosk_users = kiosk_users
        service.execute(params)

        # Email address and name are the one chosen on creation
        self.assertEqual(service.kiosk_user.email_address.email, email)
        self.assertEqual(service.kiosk_user.first_name, first_name)
        self.assertEqual(service.kiosk_user.last_name, None)
