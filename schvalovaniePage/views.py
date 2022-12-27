from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# show view only if user is logged in
@login_required(login_url='loginPage')
def schvalovanie(request):
    return render(request, 'schvalovaniePage/schvalovaniePage.html')



