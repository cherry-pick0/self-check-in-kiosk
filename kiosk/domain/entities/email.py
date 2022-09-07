from domain.entities.base_entity import BaseEntity
from domain.value_objects.email_address import EmailAddress


class Email(BaseEntity):
    _email_address: EmailAddress
    _name: str
    _subject: str
    _body: str
    _status: str

    def __init__(
        self,
        email_address,
        name,
        subject,
        body,
        status=None,
        entity_id_value=None,
    ):
        super().__init__(entity_id_value)
        self.email_address = email_address
        self.name = name
        self.subject = subject
        self.body = body
        self.status = status

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

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value: str):
        self._subject = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value: str):
        self._body = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value
