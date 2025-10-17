from rest_framework import serializers
from .models import Hotel, Room, RoomType

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'address']



class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['name', 'description', 'price_per_night', 'number_of_beds']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel', 'room_type', 'room_number', 'is_available', 'floor']
