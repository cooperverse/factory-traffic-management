from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SensorEvent
from .serializers import SensorEventSerializer
from .services import process_sensor_event


class SensorEventCreateView(generics.CreateAPIView):
    queryset = SensorEvent.objects.all()
    serializer_class = SensorEventSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        event = serializer.save()
        event = process_sensor_event(event.event_id)
        response_serializer = self.get_serializer(event)
        
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )


class SensorEventListView(generics.ListAPIView):
    queryset = SensorEvent.objects.select_related("junction").order_by("-received_at")
    serializer_class = SensorEventSerializer
