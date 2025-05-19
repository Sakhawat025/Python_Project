from django.contrib import admin
from .models import Author, Category, product, CarWashBooking, CarRental

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(product)
admin.site.register(CarWashBooking)
admin.site.register(CarRental)
