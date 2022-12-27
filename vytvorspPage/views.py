from django.shortcuts import render

# Create your views here.

def vytvorsp(request):
    return render(request, 'vytvorspPage/vytvorspPage.html')