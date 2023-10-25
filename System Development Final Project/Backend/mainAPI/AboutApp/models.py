from django.db import models

# Create your models here.
class About(models.Model):
    ProfileID = models.IntegerField(primary_key=True)
    Phone = models.CharField(max_length=2000)
    Profession = models.CharField(max_length=2000)
    Location = models.CharField(max_length=2000)
    Gender = models.IntegerField(blank=True, null=True)
    skill = models.CharField(max_length=3000)
    