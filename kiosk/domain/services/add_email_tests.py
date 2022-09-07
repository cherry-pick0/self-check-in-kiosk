from unittest import TestCase

from domain.entities.email import Email
from domain.services.add_email import (
    AddEmailEmailsIRepository,
    AddEmailParams,
    ServiceAddEmail,
)


class AddEmailTestsEmailsRepository(AddEmailEmailsIRepository):
    __email = None

    def add(self, email: Email):
        self.__email = email
        return email


class ServiceAddEmailTests(TestCase):
    def test_add_email(self):
        # Add a new Email
        email = "test@kiosk.com"
        name = "name"
        subject = "subject"
        body = "body"
        data = {"email": email, "name": name, "subject": subject, "body": body}
        params = AddEmailParams(data)
        emails = AddEmailTestsEmailsRepository()

        service = ServiceAddEmail()
        service.emails = emails
        service.execute(params)

        # Email address and name are the one chosen on creation
        self.assertEqual(service.email.email_address.email, email)
        self.assertEqual(service.email.name, name)
        self.assertEqual(service.email.subject, subject)
        self.assertEqual(service.email.body, body)
