from django.shortcuts import render

# Create your views here.

def JsomPage(request):
    return render(request,'JsomPage/jsom.html')