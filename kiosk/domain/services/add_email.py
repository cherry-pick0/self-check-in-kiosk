import abc

from domain.entities.email import Email
from domain.value_objects.email_address import EmailAddress


class AddEmailEmailsIRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, email: Email):
        pass


class AddEmailParams:
    data = None

    def __init__(self, data):
        self.data = data

    @property
    def email_address(self) -> EmailAddress:
        return EmailAddress(self.data.get("email"))

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def subject(self) -> str:
        return self.data.get("subject")

    @property
    def body(self) -> str:
        return self.data.get("body")


class ServiceAddEmail:
    __email = None
    emails: AddEmailEmailsIRepository = None

    def execute(self, params: AddEmailParams):
        email_entity = Email(
            params.email_address, params.name, params.subject, params.body
        )
        self.__email = self.emails.add(email_entity)

    @property
    def email(self):
        # Read-only; ORM or another object
        return self.__email
