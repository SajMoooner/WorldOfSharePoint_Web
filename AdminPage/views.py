from django.shortcuts import render

# Create your views here.

def AdminPage(request):
    return render(request,'AdminPage/admin.html')