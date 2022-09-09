import abc

from domain.entities.kiosk_user import KioskUser


class IDomainEvent(abc.ABC):
    time_event_raised = None


class KioskUserAdded(IDomainEvent):
    kiosk_user: KioskUser = None

    def __init__(self, kiosk_user: KioskUser):
        self.kiosk_user = kiosk_user
