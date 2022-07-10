from http.client import OK
from django.shortcuts import redirect, render
from datetime import date
from accounts.models import Account
import datetime
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate,login


def log_in_view(request):
    
    if request.method == "POST":
        password = request.POST.get("password")
        # entry = Account.objects.filter(username=username)
        username = request.POST.get("username")
        email = email = request.POST.get("username")
        user = None
        if '@' not in username:
            user_queryset = Account.objects.filter(username=username)
            user = authenticate(request,username=username,password=password)
        else:  
            user_queryset = Account.objects.filter(email=email)
            user = authenticate(request,email=email,password=password)
        input_password = user_queryset.filter(password=password)
        if not user_queryset or not input_password:
            context = {'error':'Username or password is incorrect'}
            return render(request,"home_view.html",context)
        
        context = {
            "object":user_queryset,
        }
        if user is not None:
            login(request,user)
            # printContext(context)
            # return redirect('/user',context=context)
            # return render(request,"user/home_view.html",context=context)
            return user_home_view(request,context)

        # return redirect('/user')
    return render(request,"home_view.html",{})
    

# registration

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
        
    return render(request,"register.html",{})

def validatePassword(password,confirm_password):
    context = {}
    if password != confirm_password:
        context = {"error": "Passwords, do not match"}
    if len(password) < 8:
        context = {"error": "Password must be at least 8 characters longer"}
    return context

def user_home_view(request,context):
    return render(request,"user/home_view.html",context=context)
    # return render(request,"user/home_test.html",context=c)


def user_modal_data():
    pass