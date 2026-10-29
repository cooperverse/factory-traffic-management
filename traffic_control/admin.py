from django.contrib import admin
from .models import VehicleQueueEntry, JunctionControlState
# Register your models here.
admin.site.register(VehicleQueueEntry)
admin.site.register(JunctionControlState)
