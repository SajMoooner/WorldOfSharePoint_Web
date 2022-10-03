from django.shortcuts import render

# Create your views here.

def CsomPage(request):
    return render(request,'CsomPage/CSOM.html')
