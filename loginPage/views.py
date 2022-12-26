from django.shortcuts import render

# Create your views here.

def loginPage(request):
    #loginPage/templates/loginPage/loginPage.html
    return render(request, 'loginPage/loginPage.html')


