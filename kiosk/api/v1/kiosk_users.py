from data.users.models import KioskUser
from domain.domain_events.handlers import Factory as DomainEventsFactory
from domain.services.add_email import AddEmailParams, ServiceAddEmail
from domain.services.add_kiosk_user import AddKioskUserParams, ServiceAddKioskUser
from repositories.emails import EmailsRepositoryORM
from repositories.kiosk_users import KioskUsersRepositoryORM
from rest_framework import permissions, serializers, viewsets


class KioskUsersPermissions(permissions.IsAuthenticated, permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True


class KioskUsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = KioskUser
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
        )

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        # Add a new user
        service = ServiceAddKioskUser()
        service.kiosk_users = KioskUsersRepositoryORM()
        service.domain_events_factory = DomainEventsFactory()
        params = AddKioskUserParams(validated_data)
        service.execute(params)
        added_kiosk_user = service.kiosk_user

        # todo Domain events
        # todo Registration email
        add_email_service = ServiceAddEmail()
        add_email_service.emails = EmailsRepositoryORM()
        email_data = {
            "email": added_kiosk_user.email,
            "name": added_kiosk_user.first_name,
            "subject": "",
            "body": "",
        }
        email_params = AddEmailParams(email_data)
        add_email_service.execute(email_params)

        return service.kiosk_user


class KioskUsersViewSet(
    viewsets.ModelViewSet,
):
    queryset = KioskUser.objects.all()
    serializer_class = KioskUsersSerializer
    permission_classes = (KioskUsersPermissions,)
