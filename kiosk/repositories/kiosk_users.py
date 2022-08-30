from data.users.models import KioskUser
from domain.entities.kiosk_user import KioskUser as KioskUserEntity
from domain.services.add_kiosk_user import AddKioskUserUsersIRepository
from domain.value_objects.email_address import EmailAddress


class KioskUsersRepositoryORM(AddKioskUserUsersIRepository):
    def add(self, kiosk_user_entity: KioskUserEntity):
        kiosk_user = KioskUser.objects.create(
            email=kiosk_user_entity.email_address.email,
            first_name=kiosk_user_entity.first_name,
            last_name=kiosk_user_entity.last_name,
        )
        return kiosk_user

    def get_by_id(self, kiosk_user_id: int) -> KioskUserEntity:
        kiosk_user = KioskUser.objects.get(id=kiosk_user_id)
        return KioskUserEntity(
            entity_id_value=kiosk_user.id,
            email_address_value=EmailAddress(kiosk_user.email),
            first_name_value=kiosk_user.first_name,
            last_name_value=kiosk_user.last_name,
        )
