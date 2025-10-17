from django.contrib import admin
from .models import Review
from unfold.admin import ModelAdmin

@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display=['comment_for_room', 'comment', 'user', 'created_at', 'rating']