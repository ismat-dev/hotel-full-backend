from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'), # hammasini bajaradi
        ('MANAGER', 'Manager'), # Mehmonxona menejeri xodimlarni, xonalarni boshqaradi
        ('RECEPTIONIST', 'Receptionist'), #  Bron va mehmonlarni ro‘yxatdan o‘tkazadi
        ('CUSTOMER', 'Customer'),# Oddiy foydalanuvchi (mehmon)
        ('ACCOUNTANT', 'Accountant'), # tulovlar ga 
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
