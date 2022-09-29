# https://realpython.com/asynchronous-tasks-with-django-and-celery
from celery import Celery

celery_app = Celery("celery_app", broker="redis://localhost:6379/0")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@celery_app.task
def send_emails():
    print("This is a test for send_emails()")
    from data.emails.models import DataModelEmail

    DataModelEmail.objects.update(status=DataModelEmail.ERROR)
