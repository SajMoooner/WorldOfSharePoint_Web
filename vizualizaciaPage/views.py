from django.shortcuts import render

# Create your views here.

def vizualizacia(request):
    return render(request, 'vizualizaciaPage/vizualizaciaPage.html')
