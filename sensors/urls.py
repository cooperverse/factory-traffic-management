
from django.urls import path
from .views import SensorEventCreateView, SensorEventListView

urlpatterns = [
    path("events/", SensorEventListView.as_view(), name="sensor-event-list"),
    path("events/submit/", SensorEventCreateView.as_view(), name="sensor-event-create")
]
