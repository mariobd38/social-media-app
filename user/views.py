import datetime
from datetime import date
from django.shortcuts import render,redirect
from accounts.models import Account
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

def register_view(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        email = request.POST.get("email")

        password_context = validatePassword(password,confirm_password)
        if(password_context.get('error')):
            return render(request,"register.html",password_context)

        dob = request.POST.get("dob")
        if dob == "":
            context = {"error":"Please enter your birth year"}
            return render(request,"register.html",context)

        dob = list(map(int,request.POST.get("dob").split('-')))
        dob = datetime.date(dob[0],dob[1],dob[2])
        legal_date = datetime.date(date.today().year-16,date.today().month,date.today().day)
        gender = request.POST.get("gender")

        if legal_date < dob:
            context = {"error":"Sorry, you're not old enough to register"}
            return render(request,"register.html",context)
        
        username = email.split("@")[0]
        account_object = Account.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password,dob=dob,gender=gender)
        user = User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        account_object = Account.objects.filter(username=username)

        context = {
            "object":account_object,
        }
        if user is not None:
            login(request,user)
            
            return render(request,"user/home_view.html",context=context)
     
        # return redirect('/user',context=context)

        # return render(request,"user/home_view.html",{})
        
    return render(request,"register.html",{})

def validatePassword(password,confirm_password):
    context = {}
    if password != confirm_password:
        context = {"error": "Passwords, do not match"}
    if len(password) < 8:
        context = {"error": "Password must be at least 8 characters longer"}
    return context
def user_home_view(request):
    return render(request,"user/home_view.html",{})