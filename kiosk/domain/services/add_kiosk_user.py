import abc

from kiosk.domain.entities.kiosk_user import KioskUser


class AddKioskUserUsersIRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, kiosk_user: KioskUser) -> KioskUser:
        pass


class AddKioskUserIParams(abc.ABC):
    @property
    @abc.abstractmethod
    def kiosk_user(self) -> KioskUser:
        pass


class ServiceAddKioskUser:
    __kiosk_user: KioskUser = None
    users: AddKioskUserUsersIRepository = None

    def execute(self, params: AddKioskUserIParams):
        kiosk_user_entity = params.kiosk_user
        self.__kiosk_user = self.users.add(kiosk_user_entity)

    @property
    def kiosk_user(self) -> KioskUser:
        return self.__kiosk_user
