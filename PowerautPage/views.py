from django.shortcuts import render

# Create your views here.

def PowerAutPage(request):
    return render(request,'PowerautPage/poweraut.html')