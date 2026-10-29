from rest_framework import generics,status
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Junction
from .serializers import JunctionSerializer
from .services import create_junction

class JunctionListCreateView(generics.ListCreateAPIView):
    queryset = Junction.objects.all().order_by("id")
    serializer_class = JunctionSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            juction = create_junction(name=serializer.validated_data['name'])
        
        except IntegrityError:
            raise ValidationError({
                "name" : "A junction with this name already exists. "
            })
        response_serializer = self.get_serializer(juction)
        
        return Response(
            response_serializer.data,
            status= status.HTTP_201_CREATED
        )


class JunctionDetailView(generics.RetrieveAPIView):
    queryset = Junction.objects.all()
    serializer_class = JunctionSerializer
