from django.shortcuts import render

# Create your views here.

def homePageView(request):
    # HTML je uložené v HomePage/templates/HomePage/HomePage.html
    return render(request,'HomePage/HomePage.html')