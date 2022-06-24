from django.shortcuts import render,redirect
from datetime import date
from accounts.models import Account
from django.core.exceptions import ObjectDoesNotExist

def home_view(request):
    if request.method == "POST":
        password = request.POST.get("password")
        # entry = Account.objects.filter(username=username)
        username = request.POST.get("username")
        email = email = request.POST.get("username")
        input_user = None
        account_object = None
        if '@' not in username:
            input_user = Account.objects.filter(username=username)
            account_object = Account.objects.get(username=username)
        else:  
            input_user = Account.objects.filter(email=email)
            account_object = Account.objects.get(email=email)
        
        input_password = input_user.filter(password=password)
        if not input_user or not input_password:
            context = {'error':'Username or password is incorrect'}
            return render(request,"home_view.html",context)
        
        context = {
            "object":account_object,
        }
        return redirect('/user',context=context)
    return render(request,"home_view.html",{})

def log_in(request):
    return None