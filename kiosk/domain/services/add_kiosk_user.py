import abc

from domain.entities.kiosk_user import KioskUser
from domain.value_objects.email_address import EmailAddress


class AddKioskUserUsersIRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, kiosk_user: KioskUser) -> KioskUser:
        pass

    @abc.abstractmethod
    def get_by_id(self, kiosk_user_id: int) -> KioskUser:
        pass


class AddKioskUserParams:
    data = None

    def __init__(self, data):
        self.data = data

    @property
    def email(self) -> EmailAddress:
        return EmailAddress(self.data.get("email"))

    @property
    def first_name(self) -> str:
        return self.data.get("first_name")

    @property
    def last_name(self) -> str:
        return self.data.get("last_name")


class ServiceAddKioskUser:
    __kiosk_user = None
    kiosk_users: AddKioskUserUsersIRepository = None

    def execute(self, params: AddKioskUserParams):
        kiosk_user_entity = KioskUser(
            email_address_value=params.email,
            first_name_value=params.first_name,
            last_name_value=params.last_name,
        )
        self.__kiosk_user = self.kiosk_users.add(kiosk_user_entity)

    @property
    def kiosk_user(self):
        # Read-only; ORM or another object
        return self.__kiosk_user
