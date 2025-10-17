from django.shortcuts import render

from rest_framework import generics

# local 
from .serializers import ServiceSerializer
from .permissions import IsAdmin, IsManager, IsServiceView
from .models import Service

class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsServiceView]

class ServiceCreate(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdmin]

class ServiceUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdmin]

class ServiceaCreateByMeneger(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsManager]
    