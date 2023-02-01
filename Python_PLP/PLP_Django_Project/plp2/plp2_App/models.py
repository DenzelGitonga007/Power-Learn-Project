from django.db import models

# Create your models here.
class Application(models.Model):

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    # to return the person's details
    def __str__(self):
        return self.email

    class Meta: # meta holds info about the model
        db_table = "Applications" # the table will be called applications