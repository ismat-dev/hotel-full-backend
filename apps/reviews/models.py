from django.db import models
from apps.users.models import UserProfile
from apps.rooms.models import Room

class Review(models.Model):
    comment_for_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    