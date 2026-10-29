
from rest_framework import serializers
from .models import VehicleQueueEntry, JunctionControlState


class VehicleQueueEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleQueueEntry
        fields = "__all__"
        read_only_fields = ["id"]


class JunctionControlStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JunctionControlState
        fields = "__all__"
        read_only_fields = ["id", "updated_at"]
