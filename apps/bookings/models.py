from django.db import models
from apps.rooms.models import Room
from apps.users.models import UserProfile

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.room)