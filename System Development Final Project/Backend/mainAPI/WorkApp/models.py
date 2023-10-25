from django.db import models

# Create your models here.
class Work(models.Model):
    WorkID = models.AutoField(primary_key=True)
    ProfileID = models.IntegerField(blank=True)
    ProfileName = models.CharField(max_length=100)
    ProfilePicture = models.CharField(max_length=2000,blank = True)
    ProfileRating = models.FloatField(blank=True)
    WorkTittle = models.CharField(max_length=20000)
    WorkPicture = models.CharField(max_length=2000)
    WorkRating = models.FloatField(blank=True)
    WorkReview = models.IntegerField(blank=True)
    StartingMoney = models.IntegerField(blank=True)
    WorkSummery = models.CharField(max_length=20000000000000)
    WorkDetails = models.CharField(max_length=2000000000000000000000000)
    WorkCatagory = models.CharField(max_length=20000)
    workSubCatagory = models.CharField(max_length=20000 , null=True)

class Catagory(models.Model):
    CatID = models.IntegerField(primary_key=True)
    CatSub = models.CharField(max_length=20000000000000000000) 