from django.db import models
import uuid

class ControllerCommand(models.Model):

    class CommandType(models.TextChoices):
        SET_SIGNAL_STATE = "SET_SIGNAL_STATE", "Set signal state"
        MANUAL_GREEN_REQUEST = "MANUAL_GREEN_REQUEST", "Manual green request"
        RETURN_TO_AUTOMATIC = "RETURN_TO_AUTOMATIC", "Return to automatic"
        EMERGENCY_PREEMPTION = "EMERGENCY_PREEMPTION", "Emergency preemption"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACKNOWLEDGED = "ACKNOWLEDGED", "Acknowledged"
        FAILED = "FAILED", "Failed"
        TIMED_OUT = "TIMED_OUT", "Timed out"
        CANCELLED = "CANCELLED", "Cancelled"

    command_id = models.UUIDField( default=uuid.uuid4, unique=True, editable=False)
    junction = models.ForeignKey( "junctions.Junction", on_delete=models.PROTECT, related_name="controller_commands")
    command_type = models.CharField( max_length=30, choices=CommandType.choices)
    direction = models.CharField( max_length=10, blank=True)
    requested_state = models.CharField( max_length=10, blank=True)
    status = models.CharField( max_length=15, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    acknowledged_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True)

    def __str__(self):
        return str(self.command_id)

class ControllerEvent(models.Model):

    class EventType(models.TextChoices):
        ACK = "ACK", "Acknowledgement"
        NACK = "NACK", "Negative acknowledgement"
        DEVICE_STATUS = "DEVICE_STATUS", "Device status"

    event_id = models.CharField( max_length=100, unique=True)
    junction = models.ForeignKey( "junctions.Junction", on_delete=models.PROTECT, related_name="controller_events")
    command = models.ForeignKey( ControllerCommand, on_delete=models.PROTECT, related_name="controller_events", null=True, blank=True)
    event_type = models.CharField( max_length=20, choices=EventType.choices)
    status = models.CharField(max_length=30, blank=True)
    actual_state = models.CharField(max_length=10, blank=True)
    timestamp = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.event_id} - {self.event_type}"

class DeviceStatus(models.Model):

    class DeviceType(models.TextChoices):
        SIGNAL_CONTROLLER = "SIGNAL_CONTROLLER", "Signal controller"
        SENSOR = "SENSOR", "Sensor"

    class Status(models.TextChoices):
        UNKNOWN = "UNKNOWN", "Unknown"
        ONLINE = "ONLINE", "Online"
        OFFLINE = "OFFLINE", "Offline"
        DEGRADED = "DEGRADED", "Degraded"

    junction = models.ForeignKey( "junctions.Junction", on_delete=models.PROTECT, related_name="device_statuses")
    device_type = models.CharField( max_length=30, choices=DeviceType.choices)
    direction = models.CharField( max_length=10, blank=True)
    status = models.CharField( max_length=10, choices=Status.choices, default=Status.UNKNOWN)
    last_seen_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    details = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.junction.name} - {self.device_type}"