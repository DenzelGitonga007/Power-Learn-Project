from django.contrib import admin
# from the houseApp folder, and in the models file, import the class houseListingModel
from .models import houseListingModel 

# Register your models here.
admin.site.register(houseListingModel)