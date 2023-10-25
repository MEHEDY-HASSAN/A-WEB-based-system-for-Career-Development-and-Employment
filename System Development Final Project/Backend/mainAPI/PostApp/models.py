from django.db import models

# Create your models here.
class Post(models.Model):
    PostID = models.AutoField(primary_key=True)
    ProfileID = models.IntegerField(blank=True)
    ProfileName = models.CharField(max_length=100)
    ProfilePicture = models.CharField(max_length=2000,blank = True)
    PostDate = models.DateTimeField(auto_now_add=True)
    PostImage = models.CharField(max_length=2000, blank=True)
    PostMessage = models.CharField(max_length=2000, blank=True)
    PostLikeCnt = models.IntegerField(blank=True)
    PostLikeList = models.CharField(max_length=200000000000, blank=True)
    PostCommentCnt = models.IntegerField(blank=True)
    PostCommentList = models.CharField(max_length=20000000000, blank= True )
    PostTag = models.CharField(max_length=20000, blank=True)