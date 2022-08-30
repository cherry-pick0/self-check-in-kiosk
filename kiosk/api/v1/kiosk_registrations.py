from data.registrations.models import KioskRegistration
from rest_framework import serializers, viewsets


class KioskRegistrationsSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class KioskRegistrationsViewSet(
    viewsets.ModelViewSet,
):
    queryset = KioskRegistration.objects.all()
    serializer_class = KioskRegistrationsSerializer
