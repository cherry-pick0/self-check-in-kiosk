from data.managers.models import KioskManager
from rest_framework import permissions, serializers, viewsets


class KioskManagersPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True


class KioskManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = KioskManager
        fields = ("kiosk_user",)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class KioskManagersViewSet(viewsets.ModelViewSet):
    queryset = KioskManager.objects.all()
    serializer_class = KioskManagersSerializer
    permission_classes = (KioskManagersPermissions,)
