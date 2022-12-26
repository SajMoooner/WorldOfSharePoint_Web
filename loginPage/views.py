from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .import models

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login Success")
            return render(request, 'homePage/homePage.html')
        else:
            print("Login Failed")
            logout(request)
            print(request.user.is_authenticated)
            return render(request, 'loginPage/loginPage.html')


    return render(request, 'loginPage/loginPage.html')


