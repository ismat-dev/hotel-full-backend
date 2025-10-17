from django.contrib import admin
from .models import Service
from unfold.admin import ModelAdmin

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display=['hotel', 'name', 'description', 'price', 'is_active', 'created_at']