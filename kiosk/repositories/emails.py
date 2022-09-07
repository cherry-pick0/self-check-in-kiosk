from data.emails.models import DataModelEmail
from domain.entities.email import Email as EmailEntity
from domain.services.add_email import AddEmailEmailsIRepository


class EmailsRepositoryORM(AddEmailEmailsIRepository):
    def add(self, email_entity: EmailEntity):
        email = DataModelEmail.objects.create(
            receiver_email=email_entity.email_address.email,
            receiver_name=email_entity.name,
            subject=email_entity.subject,
            body=email_entity.body,
        )
        return email
