from django.shortcuts import render

# Create your views here.

def schvalovanie(request):
    return render(request, 'schvalovaniePage/schvalovaniePage.html')



