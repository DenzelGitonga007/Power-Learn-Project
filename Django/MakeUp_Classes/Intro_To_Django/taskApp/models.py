from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone_no = models.CharField(max_length=12)



class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
