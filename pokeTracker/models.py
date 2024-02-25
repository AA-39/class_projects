from django.db import models

class Pokemon(models.Model):
    natid = models.IntegerField(primary_key=True)
    species = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255, null=True, blank=True)
    altform = models.BooleanField()

    def __str__(self):
        return f"{self.natid} - {self.species} ({self.region}, {self.type1}, {self.type2}, Altform: {self.altform})"