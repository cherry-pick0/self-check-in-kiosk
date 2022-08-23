from kiosk.domain.entities.base_entity import BaseEntity
from kiosk.domain.value_objects.email_address import EmailAddress


class KioskUser(BaseEntity):
    _email_address: EmailAddress
    _name: str

    def __init__(self, entity_id_value, email_address_value, name_value):
        super().__init__(entity_id_value)
        self.email_address = email_address_value
        self.name = name_value

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value: EmailAddress):
        if not isinstance(value, EmailAddress):
            raise TypeError

        self._email_address = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
