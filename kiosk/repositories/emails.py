from data.emails.models import DataModelEmail
from domain.entities.email import Email
from domain.entities.email import Email as EmailEntity
from domain.services.add_email import AddEmailEmailsIRepository
from domain.services.send_email import SendEmailEmailsIRepository


class EmailsRepositoryORM(AddEmailEmailsIRepository, SendEmailEmailsIRepository):
    def update_status(self, email: Email, status, error_message=""):
        DataModelEmail.objects.filter(id=email.entity_id).update(
            status=status, error_message=error_message
        )

    def add(self, email_entity: EmailEntity):
        email = DataModelEmail.objects.create(
            receiver_email=email_entity.email_address.email,
            receiver_name=email_entity.name,
            subject=email_entity.subject,
            body=email_entity.body,
        )
        return email
