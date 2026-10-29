
from rest_framework import serializers
from .models import ControllerCommand, ControllerEvent, DeviceStatus


class ControllerCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControllerCommand
        fields = "__all__"
        read_only_fields = [ "id", "command_id", "status", "created_at", "sent_at", "acknowledged_at", "error_message"]


class ControllerEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControllerEvent
        fields = "__all__"
        read_only_fields = ["id", "received_at"]


class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = "__all__"
        read_only_fields = ["id", "updated_at"]
