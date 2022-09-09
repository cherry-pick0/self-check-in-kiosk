import abc

from domain.domain_events.events import IDomainEvent, KioskUserAdded
from domain.services.add_email import AddEmailParams, ServiceAddEmail


class IDomainEventHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, domain_event: IDomainEvent):
        pass


class KioskUserAddedHandler(IDomainEventHandler):
    def handle(self, domain_event: KioskUserAdded):
        kiosk_user = domain_event.kiosk_user

        from domain.services.factory import ServiceFactory

        add_email_service = ServiceFactory().build(ServiceAddEmail)
        email_data = {
            "email": kiosk_user.email_address.email,
            "name": kiosk_user.first_name,
            "subject": "",
            "body": "",
        }
        email_params = AddEmailParams(email_data)
        add_email_service.execute(email_params)
