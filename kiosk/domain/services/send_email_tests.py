import os
from unittest import TestCase, mock

from domain.entities.email import Email
from domain.services.send_email import (
    SendEmailEmailIGateway,
    SendEmailEmailsIRepository,
    SendEmailParams,
    ServiceSendEmail,
)
from domain.value_objects.email_address import EmailAddress


class SendEmailTestEmailGateway(SendEmailEmailIGateway):
    def send(
        self, recipient: str, sender: str, subject: str, body_text: str, body_html: str
    ):
        # Do nothing
        # On application level, the gateway can be AWS SES for example
        pass


class SendEmailTestsEmailsRepository(SendEmailEmailsIRepository):
    __email = None

    def update_status(self, email: Email, status, error_message=""):
        pass


class ServiceSendEmailTests(TestCase):
    @mock.patch.dict(os.environ, {"SEND_EMAILS": "True"})
    def test_send_email(self):
        email_address = EmailAddress("test@kiosk.com")
        name = "name"
        subject = "subject"
        body = "body"
        email = Email(
            email_address, name, subject, body, status=Email.QUEUE, entity_id_value=0
        )
        params = SendEmailParams({"email": email})
        emails = SendEmailTestsEmailsRepository()
        gateway = SendEmailTestEmailGateway()

        service = ServiceSendEmail()
        service.emails = emails
        service.gateway = gateway

        service.execute(params)

    def test_send_email_fails(self):
        email_address = EmailAddress("test@kiosk.com")
        name = "name"
        subject = "subject"
        body = "body"
        email = Email(
            email_address, name, subject, body, status=Email.QUEUE, entity_id_value=0
        )
        params = SendEmailParams({"email": email})
        emails = SendEmailTestsEmailsRepository()
        gateway = SendEmailTestEmailGateway()

        service = ServiceSendEmail()
        service.emails = emails
        service.gateway = gateway

        with self.assertRaises(Exception):
            service.execute(params)
