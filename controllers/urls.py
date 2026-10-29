from django.urls import path
from .views import ControllerCommandListView, ControllerEventCreateView, ControllerEventListView, DeviceStatusListView

urlpatterns = [
    path("commands/", ControllerCommandListView.as_view(), name="controller-command-list"),
    path("events/", ControllerEventListView.as_view(), name="controller-event-list"),
    path( "events/submit/", ControllerEventCreateView.as_view(), name="controller-event-create", ),
    path("devices/", DeviceStatusListView.as_view(), name="device-status-list")
]
