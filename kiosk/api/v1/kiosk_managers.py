from data.managers.models import KioskManager
from rest_framework import serializers, viewsets


class KioskManagersSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class KioskManagersViewSet(
    viewsets.ModelViewSet,
):
    queryset = KioskManager.objects.all()
    serializer_class = KioskManagersSerializer
