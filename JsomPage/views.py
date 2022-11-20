from django.shortcuts import render, redirect
from .forms import  PridajClanok, UpravClanok
import psycopg2

# connect to the database
conn = psycopg2.connect("dbname='worldofsharepointdb' user='postgres' host='localhost' password='simonkoo'")
cur = conn.cursor()

def JsomPage(request):
    if request.method == 'POST':
        form = PridajClanok(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            typClanku = data['typClanku']
            print(typClanku)

            if typClanku == 'HOME':
                cur.execute("INSERT INTO clanokHome (nazovClanku, clanok, obrazok) VALUES (%s, %s, %s)",(data['nazov'], data['clanok'], data['obrazok']))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            elif typClanku == 'CSOM':
                cur.execute("INSERT INTO clanokCsom (nazovClanku, clanok, obrazok) VALUES (%s, %s, %s)",(data['nazov'], data['clanok'], data['obrazok']))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            elif typClanku == 'SSOM':
                cur.execute("INSERT INTO clanokSsom (nazovClanku, clanok, obrazok) VALUES (%s, %s, %s)",(data['nazov'], data['clanok'], data['obrazok']))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            else:
                return redirect('http://127.0.0.1:8000')
    else:
        form = PridajClanok()

    return render(request, 'JsomPage/jsom.html', {'form': form})

