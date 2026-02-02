from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def  login_view(request):
    return render(request,"login.html")
    
def register(request):
    return render(request,"register.html")