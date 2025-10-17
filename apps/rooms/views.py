from django.shortcuts import render
from rest_framework import generics

# local
from . serializers import HotelSerializer, RoomSerializer
from .permissions import IsAdmin
from .models import Hotel, Room


class Roomsviews(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdmin]


class RoomsUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdmin]