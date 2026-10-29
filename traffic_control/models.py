from django.db import models


class VehicleQueueEntry(models.Model):

    class Direction(models.TextChoices):
        NORTH = "NORTH", "North"
        SOUTH = "SOUTH", "South"
        EAST = "EAST", "East"
        WEST = "WEST", "West"

    junction = models.ForeignKey("junctions.Junction", on_delete=models.PROTECT, related_name="waiting_vehicles" )
    vehicle_id = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=30)
    direction = models.CharField(max_length=10, choices=Direction.choices )
    arrival_time = models.DateTimeField()
    last_event = models.ForeignKey("sensors.SensorEvent", on_delete=models.PROTECT, related_name="queue_entries", null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle_id} - {self.direction}"


class JunctionControlState(models.Model):

    class Mode(models.TextChoices):
        AUTOMATIC = "AUTOMATIC", "Automatic"
        MANUAL = "MANUAL", "Manual"
        EMERGENCY = "EMERGENCY", "Emergency"
        DEGRADED = "DEGRADED", "Degraded"

    class Phase(models.TextChoices):
        NORTH_SOUTH = "NORTH_SOUTH", "North-South"
        EAST_WEST = "EAST_WEST", "East-West"
        ALL_RED = "ALL_RED", "All Red"
        UNKNOWN = "UNKNOWN", "Unknown"

    class TransitionStatus(models.TextChoices):
        IDLE = "IDLE", "Idle"
        YELLOW = "YELLOW", "Yellow transition"
        ALL_RED = "ALL_RED", "All-red clearance"
        WAITING_ACK = "WAITING_ACK", "Waiting for acknowledgement"

    junction = models.OneToOneField( "junctions.Junction", on_delete=models.PROTECT, related_name="control_state" )
    mode = models.CharField(max_length=10, choices=Mode.choices,default=Mode.AUTOMATIC )
    current_phase = models.CharField( max_length=20, choices=Phase.choices, default=Phase.UNKNOWN)
    transition_status = models.CharField( max_length=20, choices=TransitionStatus.choices, default=TransitionStatus.IDLE )
    emergency_active = models.BooleanField(default=False)
    manual_direction = models.CharField( max_length=10, choices=VehicleQueueEntry.Direction.choices, null=True, blank=True )
    phase_started_at = models.DateTimeField( null=True, blank=True)
    transition_started_at = models.DateTimeField( null=True, blank=True )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.junction.name} - {self.mode}"
