from django.shortcuts import render
from rest_framework import generics
from .models import JunctionControlState, VehicleQueueEntry
from .serializers import   JunctionControlStateSerializer, VehicleQueueEntrySerializer


class JunctionControlStateListView(generics.ListAPIView):
    queryset = JunctionControlState.objects.select_related("junction")
    serializer_class = JunctionControlStateSerializer


class JunctionControlStateDetailView(generics.RetrieveAPIView):
    queryset = JunctionControlState.objects.select_related("junction")
    serializer_class = JunctionControlStateSerializer


class VehicleQueueListView(generics.ListAPIView):
    queryset = VehicleQueueEntry.objects.select_related("junction").order_by("arrival_time")
    serializer_class = VehicleQueueEntrySerializer
