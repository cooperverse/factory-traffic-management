from django.db import models

class SensorEvent(models.Model):
    
    class EventType(models.TextChoices):
        VEHICLE_ARRIVED = "ARRIVED", "Vehicle arrived"
        VEHICLE_CLEARED = "CLEARED", "Vehicle cleared"
        
    class ProcessingStatus(models.TextChoices):
        RECEIVED = "RECEIVED", "Received"
        PROCESSED = "PROCESSED", "Processed"
        REJECTED = "REJECTED", "Rejected"
        FAILED = "FAILED", "Failed"
        
    class Direction(models.TextChoices):
        NORTH = "NORTH", "North"
        SOUTH = "SOUTH", "South"
        EAST = "EAST", "East"
        WEST = "WEST", "West"
        
    event_id = models.CharField(max_length=100, unique=True)
    junction = models.ForeignKey("junctions.Junction", on_delete=models.PROTECT, related_name="sensor_events")
    vehicle_id = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=30, blank=True)
    direction = models.CharField(max_length=10, choices=Direction.choices)
    event_type = models.CharField(max_length=15, choices=EventType.choices )
    sequence_no = models.PositiveBigIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)
    processing_status = models.CharField(max_length=10, choices=ProcessingStatus.choices, default=ProcessingStatus.RECEIVED )
    rejection_reason = models.TextField(blank=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.event_id} - {self.event_type}"
