from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=50) 
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_beds = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, related_name='rooms')
    room_number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)
    floor = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number} ({self.room_type.name if self.room_type else 'N/A'})"
    
    def get_price(self):
        return self.room_type.price_per_night if self.room_type else 0