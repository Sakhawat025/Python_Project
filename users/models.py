from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    membership_type = models.CharField(max_length=20, blank=True, null=True)
    profile_images = models.ImageField(upload_to='profile_images/', blank=True, null=True)
