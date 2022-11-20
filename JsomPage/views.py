from django.shortcuts import render, redirect
from .forms import  PridajClanok

# Create your views here.

def JsomPage(request):
    if request.method == 'POST':
        form = PridajClanok(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('http://127.0.0.1:8000')
    else:
        form = PridajClanok()
    return render(request, 'JsomPage/jsom.html', {'form': form})


