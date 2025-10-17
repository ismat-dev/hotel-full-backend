from django.db import models
from apps.users.models import UserProfile
from apps.rooms.models import Room

class Review(models.Model):
    comment_for_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    created_at = models.DateField(auto_now=True)
    