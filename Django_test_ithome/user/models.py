from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class UserProfile(AbstractUser):
    id  = models.CharField(max_length=150,primary_key=True)
    account  = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    createtime = models.DateTimeField(auto_now_add=True,auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self) :
        return self.account
# Create your models here.
