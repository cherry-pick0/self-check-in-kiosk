from domain.services.add_email import ServiceAddEmail
from domain.services.add_kiosk_user import ServiceAddKioskUser
from repositories.emails import EmailsRepositoryORM
from repositories.kiosk_users import KioskUsersRepositoryORM


def add_kiosk_user():
    service = ServiceAddKioskUser()
    service.kiosk_users = KioskUsersRepositoryORM()
    return service


def add_email():
    service = ServiceAddEmail()
    service.emails = EmailsRepositoryORM()
    return service


class ServiceFactory:
    services = {
        ServiceAddKioskUser: add_kiosk_user,
        ServiceAddEmail: add_email,
    }

    def build(self, service_class_key):
        service_class = self.services.get(service_class_key)
        service = service_class()

        # Put event handler logic here
        # todo find better solution
        from domain.domain_events.factory import DomainEventsFactory

        service.domain_events_factory = DomainEventsFactory()

        return service
