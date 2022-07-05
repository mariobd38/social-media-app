from django.shortcuts import render
from datetime import date
from accounts.models import Account
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login

def log_in_view(request):
    
    if request.method == "POST":
        password = request.POST.get("password")
        # entry = Account.objects.filter(username=username)
        username = request.POST.get("username")
        email = email = request.POST.get("username")
        input_user = None
        user = None
        if '@' not in username:
            input_user = Account.objects.filter(username=username)
            user = authenticate(request,username=username,password=password)
        else:  
            input_user = Account.objects.filter(email=email)
            user = authenticate(request,email=email,password=password)
        input_password = input_user.filter(password=password)
        if not input_user or not input_password:
            context = {'error':'Username or password is incorrect'}
            return render(request,"home_view.html",context)
        
        context = {
            "object":input_user,
        }
        print(user)
        if user is not None:
            login(request,user)
            
            return render(request,"user/home_view.html",context=context)
        # return redirect('/user',context=context)
        # return redirect('/user')
    return render(request,"home_view.html",{})