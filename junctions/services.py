from django.db import transaction
from .models import Junction, SignalState
from traffic_control.models import JunctionControlState
@transaction.atomic
def create_junction(name):
    junction = Junction.objects.create(name=name)
    
    JunctionControlState.objects.create(junction=junction)
    
    for direction, _ in SignalState.Direction.choices:
        SignalState.objects.create(
            junction=junction,
            direction=direction
        )
    return junction