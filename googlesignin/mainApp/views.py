from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'login.html')

@login_required
def home(request):
    fname=request.user.first_name
    lname=request.user.last_name
    email=request.user.email
    contex={
        'fname':fname,
        'lname':lname,
        'email':email
    }
    return render(request,'home.html',contex)

def logout(request):
    return render(request,'login.html')