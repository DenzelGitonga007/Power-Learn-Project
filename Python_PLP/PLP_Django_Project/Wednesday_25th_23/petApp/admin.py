from django.contrib import admin
# Import the models
from .models import Vaccines, Pet

# Register your models here.
admin.site.register(Pet)
admin.site.register(Vaccines)
