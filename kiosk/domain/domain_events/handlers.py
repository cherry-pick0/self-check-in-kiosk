import abc

from domain.domain_events.events import IDomainEvent, KioskUserAdded


class IDomainEventHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, domain_event: IDomainEvent):
        pass


class KioskUserAddedHandler(IDomainEventHandler):
    def handle(self, domain_event: KioskUserAdded):
        from data.emails.models import DataModelEmail

        DataModelEmail.objects.all()


class Factory:
    def __init__(self):
        self.domain_events = {KioskUserAdded: [KioskUserAddedHandler]}

    def raise_domain_events(self, domain_event_class, **kwargs):
        handlers = self.domain_events.get(domain_event_class)
        domain_event = domain_event_class(**kwargs)

        for handler_class in handlers:
            handler = handler_class()
            handler.handle(domain_event)
