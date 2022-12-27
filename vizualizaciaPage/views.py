from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# show view only if user is logged in

def vizualizacia(request):
    return render(request, 'vizualizaciaPage/vizualizaciaPage.html')
