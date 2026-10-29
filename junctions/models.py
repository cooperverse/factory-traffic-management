from django.db import models

class Junction(models.Model):
    name = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class SignalState(models.Model):
    
    class Direction(models.TextChoices):
        NORTH = "NORTH", "North"
        SOUTH = "SOUTH", "South"
        EAST = "EAST", "East"
        WEST = "WEST", "West"
    
    class State(models.TextChoices):
        UNKNOWN = "UNKNOWN", "Unknown"
        RED = "RED", "Red"
        YELLOW = "YELLOW", "Yellow"
        GREEN = "GREEN", "Green"
    
    junction = models.ForeignKey(Junction, on_delete=models.PROTECT, related_name="signals")
    direction = models.CharField(max_length=20, choices=Direction.choices)
    desired_state = models.CharField(max_length=20, choices=State.choices, default=State.RED)
    actual_state = models.CharField(max_length=20, choices=State.choices, default=State.UNKNOWN)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.junction.name} - {self.direction}"