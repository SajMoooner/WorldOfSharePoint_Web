from django.shortcuts import render

# Create your views here.

def SsomPageView(request):
    return render(request,'SsomPage/ssom.html')