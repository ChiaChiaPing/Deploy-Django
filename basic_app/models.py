from django.db import models
from django.contrib.auth.models import User # like auth 的 data model 底下的 User(想像成是一張資料表)

# Create your models here.

class UserInfoProfile(models.Model):

    # OneToOne => uinque and Forieign key
    # auth,models 的 User 當成我的外鍵 => user 同時要當成我這個資料表的主鍵
    user = models.OneToOneField(User,on_delete="CASADE") # auth user 當成 這個 UserInforProfile 的外鍵 => user

    # addidtional
    portfolio_site=models.URLField(blank=True)

    profile_pics=models.ImageField(upload_to='profile_pics',blank=True) #blank 代表user可以不填
    
    def __str__(self):
        return self.user.username

    


