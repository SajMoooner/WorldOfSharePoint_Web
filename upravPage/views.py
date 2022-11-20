from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import  UpravClanok
import psycopg2

# connect to the database
conn = psycopg2.connect("dbname='worldofsharepointdb' user='postgres' host='localhost' password='simonkoo'")
cur = conn.cursor()

def UpravPage(request):
    if request.method == 'POST':
        form = UpravClanok(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            typClanku = data['typClanku']

            if typClanku == 'HOME':
                cur.execute("UPDATE clanokHome SET clanok = %s, obrazok = %s WHERE nazovClanku = %s",(data['clanok'], data['obrazok'], data['nazovClanku']))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            elif typClanku == 'CSOM':
                cur.execute("UPDATE clanokCsom SET clanok = %s, obrazok = %s WHERE nazovClanku = %s",(data['clanok'], data['obrazok'], data['nazovClanku']))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            elif typClanku == 'SSOM':
                cur.execute("UPDATE clanokSsom SET clanok = %s, obrazok = %s WHERE nazovClanku = %s",(data['clanok'], data['obrazok'], data['nazovClanku']))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
        else:
            return redirect('http://http://127.0.0.1:8000')
    else:
        form = UpravClanok()

    return render(request, 'upravPage/upravPage.html', {'form': form})
