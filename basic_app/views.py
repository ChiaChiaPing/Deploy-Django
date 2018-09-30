from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# package for login and logout
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request,"basic_app/index.html")

@login_required
def special(request):
    return HttpResponse("You are login in")

@login_required
def user_logout(request): # logout 回到首頁
    logout(request)
    return HttpResponseRedirect(reverse("index"))  
  

def register(request):
    registered=False
    user_form=UserForm()
    profile_form=UserProfileInfoForm()
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # for user
            user=user_form.save()
            user.set_password(user.password) # set hashing password
            user.save()

            profile=profile_form.save(commit=False) # 表單.save() 會回傳 該表單連結的 Data Model
            profile.user=user

            if 'profile_pics' in request.FILES: # for image files
                profile.profile_pics=request.FILES['profile_pics'] # profile_pics 是剛剛前面在 建立 models 針對 pic的設定

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    context={
        "registered":registered,
        "user_form":user_form,
        "profile_form":profile_form
    }

    return render(request,'basic_app/registration.html',context=context)

# login and logout functions
def user_login(request):

    if request.method=="POST":

        username=request.POST.get("username") # get form's data (from label)
        password=request.POST.get("password")

        user = authenticate(username=username,password=password) # authenticate the user

        if user: # 若有找到相對應已授權的 User
            if user.is_active:  
                login(request,user)
                return HttpResponseRedirect(reverse("index")) # redirect back to the homepage
            
            else:
                return HttpResponse("Account Not Active")
        
        else:
            print("Someone try to login and fail")
            print("Username: {} and password:{}".format(username,password))
            return HttpResponse("Invalid login details applied")
    else:
        return render(request,"basic_app/login.html",{})


