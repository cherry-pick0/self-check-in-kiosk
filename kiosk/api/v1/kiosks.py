from data.users.models import KioskUser
from domain.services.add_kiosk_user import AddKioskUserParams, ServiceAddKioskUser
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
        service = ServiceAddKioskUser()
        service.kiosk_users = KioskUsersRepositoryORM()
        params = AddKioskUserParams(validated_data)
        service.execute(params)
        return service.kiosk_user


class KioskUsersViewSet(
    viewsets.ModelViewSet,
):
    queryset = KioskUser.objects.all()
    serializer_class = KioskUsersSerializer
    permission_classes = (KioskUsersPermissions,)
