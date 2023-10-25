from email.message import Message
from email.mime import audio
from email.policy import default
from sqlite3 import Date
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Message(models.Model):
    MessageSenderID = models.IntegerField()
    MessageReceiverID = models.IntegerField()
    Message = models.CharField(max_length=10000)
    MessageSenderName = models.CharField(max_length=2000,blank = True)
    MessageReceiverName = models.CharField(max_length=2000,blank = True)
    MessageSenderProfilePicture = models.CharField(max_length=2000,blank = True)
    MessageReceiverProfilePicture = models.CharField(max_length=2000,blank = True)
    MessageSendDateTime = models.DateTimeField(auto_now_add=True)