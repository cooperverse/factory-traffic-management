from django.contrib import admin
from .models import ControllerCommand, ControllerEvent, DeviceStatus
# Register your models here.
admin.site.register(ControllerEvent)
admin.site.register(ControllerCommand)
admin.site.register(DeviceStatus)