from django.contrib import admin


# Register your models here.
from . models import Task, UserProfile
admin.site.register(Task)
admin.site.register(UserProfile)