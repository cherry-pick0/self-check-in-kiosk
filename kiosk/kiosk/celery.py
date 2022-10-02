# https://realpython.com/asynchronous-tasks-with-django-and-celery
from data.emails.models import DataModelEmail
from domain.entities.email import Email
from domain.services.factory import ServiceFactory
from domain.services.send_email import SendEmailParams, ServiceSendEmail
from domain.value_objects.email_address import EmailAddress

from celery import Celery

celery_app = Celery("celery_app", broker="redis://localhost:6379/0")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@celery_app.task
def send_emails():
    service = ServiceFactory().build(ServiceSendEmail)
    for data_model_email in DataModelEmail.objects.filter(status=DataModelEmail.QUEUE)[
        :20
    ]:
        email = Email(
            email_address=EmailAddress(data_model_email.receiver_email),
            name=data_model_email.receiver_name,
            subject=data_model_email.subject,
            body=data_model_email.body,
            status=data_model_email.status,
            entity_id_value=data_model_email.id,
        )
        params = SendEmailParams(email)
        service.execute(params)
