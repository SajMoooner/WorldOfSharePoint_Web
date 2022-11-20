from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import  VymazClanok
import psycopg2

# connect to the database
conn = psycopg2.connect("dbname='worldofsharepointdb' user='postgres' host='localhost' password='simonkoo'")
cur = conn.cursor()

def vymazPage(request):
    if request.method == 'POST':
        form = VymazClanok(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            typClanku = data['typClanku']

            if typClanku == 'HOME':
                cur.execute('DELETE FROM clanokHome WHERE nazovClanku = %s', (data['nazovClanku'],))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            elif typClanku == 'CSOM':
                cur.execute('DELETE FROM clanokCsom WHERE nazovClanku = %s', (data['nazovClanku'],))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
            elif typClanku == 'SSOM':
                cur.execute('DELETE FROM clanokSsom WHERE nazovClanku = %s', (data['nazovClanku'],))
                conn.commit()
                cur.close()
                return redirect('http://127.0.0.1:8000')
        else:
            return redirect('http://127.0.0.1:8000')
    else:
        form = VymazClanok()

    return render(request, 'vymazPage/vymazPage.html', {'form': form})

