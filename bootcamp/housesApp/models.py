from django.db import models

# Create your models here.

class houseListingModel(models.Model):
    # the attributes/fields/columns
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    square_feet = models.IntegerField()
    no_of_bedrooms = models.IntegerField()
    address = models.CharField(max_length=255)
    image = models.ImageField()
    