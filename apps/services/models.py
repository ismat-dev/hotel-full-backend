from django.db import models
from apps.rooms.models import Hotel  # agar xizmatlar har bir hotelga tegishli bo‘lsa

class Service(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.hotel.name}"
