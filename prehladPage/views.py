from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# show view only if user is logged in
@login_required(login_url='loginPage')
def prehlad(request):
    return render(request, 'prehladPage/prehladPage.html')