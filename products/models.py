from django.db import models

# Create your models here.

class Products(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()

class Country(models.Model):

    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    area = models.IntegerField(help_text="(in square kilometers)")