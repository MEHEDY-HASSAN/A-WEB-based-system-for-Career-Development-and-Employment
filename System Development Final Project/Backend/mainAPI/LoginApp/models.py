from django.db import models

# Create your models here.
class Login(models.Model):
    loginID = models.AutoField(primary_key=True)
    EmailAddress = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

