from django.contrib import admin
# Import the models
from .models import Vaccine, Pet

# Register your models here.
admin.site.register(Pet)
admin.site.register(Vaccine)

# To display the names headers
# @admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#     list_display = ('name', 'gender', 'submitted_on', 'species', 'owner', 'age')