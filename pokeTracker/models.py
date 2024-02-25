# models.py
from django.db import models

class Pokemon(models.Model):
    natid = models.IntegerField(primary_key=True)
    species = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    altform = models.BooleanField(default=False)