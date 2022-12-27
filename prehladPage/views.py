from django.shortcuts import render

# Create your views here.


def prehlad(request):
    return render(request, 'prehladPage/prehladPage.html')