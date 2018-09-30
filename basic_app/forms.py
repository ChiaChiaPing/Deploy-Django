from django import forms
from django.contrib.auth.models import User
from .models import UserInfoProfile


# form 形式是從database 選取我們要的欄位，然後抓過來的 

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=("username","email","password")

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfoProfile
        fields=("portfolio_site","profile_pics")
