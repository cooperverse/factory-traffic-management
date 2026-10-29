from django.urls import path
from .views import JunctionControlStateListView, JunctionControlStateDetailView, VehicleQueueListView

urlpatterns = [
    path("states/", JunctionControlStateListView.as_view(), name="control-state-list"),
    path("states/<int:pk>/", JunctionControlStateDetailView.as_view(), name="control-state-detail"),
    path("queue/", VehicleQueueListView.as_view(), name="vehicle-queue-list"),
]
