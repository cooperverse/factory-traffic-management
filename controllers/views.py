from django.shortcuts import render
from rest_framework import generics
from .models import ControllerCommand, ControllerEvent, DeviceStatus
from .serializers import ControllerCommandSerializer, ControllerEventSerializer, DeviceStatusSerializer


class ControllerCommandListView(generics.ListAPIView):
    queryset = ControllerCommand.objects.select_related("junction").order_by("-created_at")
    serializer_class = ControllerCommandSerializer


class ControllerEventCreateView(generics.CreateAPIView):
    queryset = ControllerEvent.objects.all()
    serializer_class = ControllerEventSerializer


class ControllerEventListView(generics.ListAPIView):
    queryset = ControllerEvent.objects.select_related("junction").order_by("-received_at")
    serializer_class = ControllerEventSerializer


class DeviceStatusListView(generics.ListAPIView):
    queryset = DeviceStatus.objects.select_related("junction")
    serializer_class = DeviceStatusSerializer

