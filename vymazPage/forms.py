from django import forms

class VymazClanok(forms.Form):
    typClanku = forms.CharField(label='Typ článku', max_length=100)
    nazovClanku = forms.CharField(label="Zadaj nazov clanku ktorý chcete vymazať",max_length=100)
