from django.shortcuts import render

# Create your views here.

def LoginPage(request):
    return render(request,'LoginPage/login.html')