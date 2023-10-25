from django.db import models

# Create your models here.
class Follow(models.Model):
    FollowID = models.IntegerField(primary_key=True)

class Active(models.Model):
    ProfileID = models.IntegerField(primary_key=True)
    ActiveTime = models.DateTimeField(auto_now=True)