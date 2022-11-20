from django import forms

class PridajClanok(forms.Form):
    typClanku = forms.CharField(label='Typ článku', max_length=100)
    nazov = forms.CharField(label="Zadaj nazov clanku",max_length=100)
    clanok = forms.CharField(label="Napíš článok" ,max_length=1000, )
    obrazok = forms.CharField(label="Obrázok",max_length=100)

