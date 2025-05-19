from django.db import models
from django.conf import settings


# ai khane dgano live opretation nah thaker jonne ai khane ai kaj backand a thake jai ,, aikhane live dekaanu possible hoy nah 

class CarWashBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    service_location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    car_details = models.CharField(max_length=200)

class CarRental(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.car_name} rented by {self.user.username}"

class Author(models.Model):
   name = models.CharField(max_length=100)
   bio = models.TextField(blank=True)
   email = models.EmailField(unique=True)
   created_at = models.DateTimeField(auto_now_add=True)
   profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
   def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.product_name


