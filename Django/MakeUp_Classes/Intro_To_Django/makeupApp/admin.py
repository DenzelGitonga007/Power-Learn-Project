from django.contrib import admin
# Import the models
from . models import Person
# Register your models here.
# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'age'
    )
    