from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['comment_for_room', 'comment', 'user', 'created_at']