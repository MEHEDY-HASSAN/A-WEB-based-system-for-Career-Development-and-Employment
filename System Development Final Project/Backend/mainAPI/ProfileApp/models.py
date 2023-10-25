from django.db import models

# Create your models here.
class Profile(models.Model):
    ProfileID = models.IntegerField(primary_key=True)
    ProfileName = models.CharField(max_length = 2000)
    ProfilePicture = models.CharField(max_length=2000,blank = True)
    ProfileCoverPhoto = models.CharField(max_length=2000,blank = True)
    ProfileBio = models.CharField(max_length=2000,blank = True)
