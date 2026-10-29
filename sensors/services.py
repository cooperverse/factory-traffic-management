from django.db import transaction
from django.utils import timezone
from .models import SensorEvent
from traffic_control.models import VehicleQueueEntry

@transaction.atomic
def process_sensor_event(event_id):
    event = SensorEvent.objects.select_for_update().get(
        event_id = event_id
    )
    
    if event.processing_status == SensorEvent.ProcessingStatus.PROCESSED:
        return event

    if event.event_type == SensorEvent.EventType.VEHICLE_ARRIVED:
        VehicleQueueEntry.objects.get_or_create(
            junction = event.junction,
            vehicle_id = event.vehicle_id,
            defaults={
                "vehicle_type": event.vehicle_type,
                "direction": event.direction,
                "arrival_time": event.timestamp,
                "last_event": event,
            }
        )
    elif event.event_type == SensorEvent.EventType.VEHICLE_CLEARED:
        VehicleQueueEntry.objects.filter(
            junction = event.junction,
            vehicle_id = event.vehicle_id,
            direction = event.direction
        ).delete()
        
    event.processing_status = SensorEvent.ProcessingStatus.PROCESSED
    event.processed_at = timezone.now()
    event.save(
        update_fields=["processing_status", "processed_at"]
    )
    return event