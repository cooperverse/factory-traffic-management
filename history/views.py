from django.shortcuts import render
from rest_framework import generics
from .models import AuditLog
from .serializers import AuditLogSerializer


class AuditLogListView(generics.ListAPIView):
    queryset = AuditLog.objects.select_related("junction", "command").order_by( "-created_at")
    serializer_class = AuditLogSerializer
