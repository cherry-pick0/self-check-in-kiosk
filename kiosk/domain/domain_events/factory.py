import abc

from domain.domain_events.events import KioskUserAdded
from domain.domain_events.handlers import KioskUserAddedHandler


class IDomainEventsRunner(abc.ABC):
    @abc.abstractmethod
    def trigger(self, *__):
        pass


class DomainEventsRunner(IDomainEventsRunner):
    def __init__(self):
        self.domain_events = {KioskUserAdded: [KioskUserAddedHandler]}

    def trigger(self, domain_event_class, **kwargs):
        handlers = self.domain_events.get(domain_event_class)
        domain_event = domain_event_class(**kwargs)

        for handler_class in handlers:
            handler = handler_class()
            handler.handle(domain_event)
