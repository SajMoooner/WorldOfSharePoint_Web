from django.shortcuts import render

# Create your views here.

def FrameworkPage(request):
    return render(request,'FrameworkPage/spfx.html')