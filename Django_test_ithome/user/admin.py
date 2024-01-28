from django.contrib import admin
from . import models #從同層資料夾(user)匯入models 
from django.contrib import admin

admin.site.register(models.UserProfile)#註冊models的UserProfile



# Register your models here.
