from django import forms

class UpravClanok(forms.Form):
    typClanku = forms.CharField(label='Typ článku', max_length=100)
    nazovClanku = forms.CharField(label="Zadaj nazov clanku",max_length=100)
    clanok = forms.CharField(label="Napíš nový článok" ,max_length=1000)
    obrazok = forms.CharField(label="Vlož nový obrázok",max_length=100)