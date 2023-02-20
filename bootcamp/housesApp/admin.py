from django.contrib import admin
# from the houseApp folder, and in the models file, import the class houseListingModel
from .models import houseListingModel 

# Register your models here.
admin.site.register(houseListingModel)

# Retrieving the data on the return self
# class houseListinAdmin(admin.ModelAdmin):
#     list_display = [
#         'title', 'price', 'square_feet'
#     ]
#     list_editable = [
#         'title', 'price', 'square_feet'
#     ]
#     prepopulated_fields = {'id':('')}
