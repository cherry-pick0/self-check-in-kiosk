from domain.entities.base_entity import BaseEntity
from domain.value_objects.email_address import EmailAddress


class KioskUser(BaseEntity):
    _email_address: EmailAddress
    _first_name: str
    _last_name: str

    def __init__(
        self,
        email_address_value,
        first_name_value=None,
        last_name_value=None,
        entity_id_value=None,
    ):
        super().__init__(entity_id_value)
        self.email_address = email_address_value
        self.first_name = first_name_value
        self.last_name = last_name_value

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value: EmailAddress):
        if not isinstance(value, EmailAddress):
            raise TypeError

        self._email_address = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"
