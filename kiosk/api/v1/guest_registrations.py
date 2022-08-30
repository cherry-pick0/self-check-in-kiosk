from data.guests.models import KioskGuest
from rest_framework import serializers, viewsets


class GuestRegistrationsSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GuestRegistrationsViewSet(
    viewsets.ModelViewSet,
):
    queryset = KioskGuest.objects.all()
    serializer_class = GuestRegistrationsSerializer
