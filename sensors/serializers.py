from rest_framework import serializers
from .models import SensorEvent


class SensorEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorEvent
        fields = "__all__"
        read_only_fields = [ "id", "received_at", "processing_status", "rejection_reason", "processed_at"]
