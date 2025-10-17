from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'user',
            'room',
            'check_in',
            'check_out',
            'created_at'
        ]
    