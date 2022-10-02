import abc
import os

from domain.entities.email import Email


class SendEmailEmailIGateway(abc.ABC):
    @abc.abstractmethod
    def send(
        self, recipient: str, sender: str, subject: str, body_text: str, body_html: str
    ):
        pass


class SendEmailEmailsIRepository(abc.ABC):
    @abc.abstractmethod
    def update_status(self, email: Email, status):
        pass


class SendEmailParams:
    data = None

    def __init__(self, data):
        self.data = data

    @property
    def email(self) -> Email:
        return self.data.get("email")


class ServiceSendEmail:
    __email = None
    emails: SendEmailEmailsIRepository = None
    gateway: SendEmailEmailIGateway = None

    def execute(self, params: SendEmailParams):
        email_entity = params.email

        if not os.environ.get("SEND_EMAILS"):
            raise Exception("Sending of emails is globally disabled")

        if not email_entity.status == Email.QUEUE:
            raise Exception("Status invalid")

        self.gateway.send(
            recipient=str(email_entity.email_address),
            sender="fakeemail@test.com",
            subject=email_entity.subject,
            body_text="",  # todo body_text
            body_html=email_entity.body,
        )

        self.emails.update_status(email_entity, Email.SENT)
