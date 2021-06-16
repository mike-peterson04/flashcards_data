from django.db import models

# Create your models here.

class Card(models.Model):
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=150)

class Collection(models.Model):
    name = models.CharField(max_length=50)