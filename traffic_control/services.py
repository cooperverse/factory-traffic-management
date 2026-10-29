from junctions.models import SignalState
from .state_machine import is_safe_green_configuration
from django.shortcuts import get_object_or_404
from .models import JunctionControlState
from junctions.models import SignalState


def get_control_state(junction_id):
    return get_object_or_404(
        JunctionControlState,
        junction_id=junction_id,
    )
    
def get_signal_states(junction_id):
    return SignalState.objects.filter(
        junction_id=junction_id
    ).order_by("direction")
    
def validate_green_directions(green_directions):
    if not is_safe_green_configuration(green_directions):
        raise ValueError(
            "Conflicting traffic phases cannot be GREEN simultaneously."
        )

    return True

def set_desired_signals(junction_id, green_directions):
    validate_green_directions(green_directions)

    signals = get_signal_states(junction_id)

    for signal in signals:
        if signal.direction in green_directions:
            signal.desired_state = SignalState.State.GREEN
        else:
            signal.desired_state = SignalState.State.RED

        signal.save(update_fields=["desired_state"])