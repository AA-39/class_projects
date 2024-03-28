## class_projects/pokeTracker/models.py
from django.db import models
from django.contrib.auth.models import User
import json

class Pokemon(models.Model):
    natid = models.IntegerField(primary_key=True)
    species = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    altform = models.BooleanField(default=False)
    link = models.CharField(max_length=255, null=True, blank=True)

class PokedexCheckedCheckbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_checkboxes = models.TextField(default='[]')

    def get_checked_checkboxes(self):
        return json.loads(self.checked_checkboxes)

    def set_checked_checkboxes(self, checked_checkboxes):
        self.checked_checkboxes = json.dumps(checked_checkboxes)

    checked_checkboxes_list = property(get_checked_checkboxes, set_checked_checkboxes)

class ShinydexCheckedCheckbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_checkboxes = models.TextField(default='[]')

    def get_checked_checkboxes(self):
        return json.loads(self.checked_checkboxes)

    def set_checked_checkboxes(self, checked_checkboxes):
        self.checked_checkboxes = json.dumps(checked_checkboxes)

    checked_checkboxes_list = property(get_checked_checkboxes, set_checked_checkboxes)