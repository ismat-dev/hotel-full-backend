from django.contrib import admin
from .models import Hotel, Room,RoomType

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display=['name', 'address']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['hotel', 'room_type', 'room_number', 'is_available', 'floor']

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display=['name', 'description', 'price_per_night', 'number_of_beds']