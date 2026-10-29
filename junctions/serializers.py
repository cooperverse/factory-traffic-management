from rest_framework import serializers
from .models import Junction, SignalState

class SignalStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalState
        fields = "__all__"
        read_only_fields = ["id", "actual_state", "updated_at"]

class JunctionSerializer(serializers.ModelSerializer):
    signals = SignalStateSerializer(many=True, read_only=True)

    class Meta:
        model = Junction
        fields = ["id", "name", "is_active", "created_at", "signals"]
        read_only_fields = ["id", "created_at"]

