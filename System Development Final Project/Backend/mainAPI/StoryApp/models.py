from django.db import models

# Create your models here.
class Story(models.Model):
    StoryID = models.AutoField(primary_key=True)
    ProfileID = models.IntegerField(blank=True)
    ProfileName = models.CharField(max_length=100)
    ProfilePicture = models.CharField(max_length=2000,blank = True)
    StoryDate = models.DateTimeField(auto_now_add=True)
    StoryImage = models.CharField(max_length=2000, blank=True)
    