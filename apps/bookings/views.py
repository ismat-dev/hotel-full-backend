from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
# local
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsUser, IsReceptionist
from apps.rooms.models import Room
from apps.rooms.serializers import RoomSerializer
from .pagination import BookingsPageNumberPagination

class MyModelCustomPaginatedListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = BookingsPageNumberPagination


class UserBookings(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsUser]
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
class UserBookingsUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class Bookings(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsReceptionist]