from django.db import models

# Create your models here.
# Two tables: pets and vaccines-- Many to many

# Create a model for vaccines model
class Vaccine(models.Model):
    # The attributes/ fields
    name = models.CharField(max_length=155, unique=True)

# Pet model/table
class Pet(models.Model):

    GENDER_CHOICES = [("M", "Male"),
    ("F", "Female")
    ] # For gender
    name = models.CharField(max_length=155)
    owner = models.CharField(max_length=155)
    submitted_on = models.DateTimeField()
    species = models.CharField(max_length=100)    
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    description = models.TextField(blank=True, null=True)

    # Relationship
    vaccines = models.ManyToManyField(Vaccine)

    # To return the name of the pet
    def __str__(self):
        return self.name