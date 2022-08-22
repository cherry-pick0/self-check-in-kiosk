from kiosk.domain.entities.base_entity import BaseEntity
from kiosk.domain.value_objects.email_address import EmailAddress


class KioskUser(BaseEntity):
    _email_address: EmailAddress

    def __init__(self, entity_id_value, email_address_value):
        super().__init__(entity_id_value)
        self.email_address = email_address_value

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value: EmailAddress):
        self._email_address = value
