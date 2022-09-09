from domain.domain_events.events import KioskUserAdded
from domain.domain_events.handlers import KioskUserAddedHandler


class DomainEventsFactory:
    def __init__(self):
        self.domain_events = {KioskUserAdded: [KioskUserAddedHandler]}

    def raise_domain_events(self, domain_event_class, **kwargs):
        handlers = self.domain_events.get(domain_event_class)
        domain_event = domain_event_class(**kwargs)

        for handler_class in handlers:
            handler = handler_class()
            handler.handle(domain_event)
