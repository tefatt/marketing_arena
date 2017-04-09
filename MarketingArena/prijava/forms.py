from django.forms import ModelForm
from prijava.models import Aplikant
from django.conf import settings
from django import forms


class Opsti_podaci(ModelForm):
#    godina_rodjenja = forms.DateField(('%d/%m/%Y',), label='godina rodjenja',  
#    widget=forms.DateTimeInput('%d/%m/%Y', attrs={
#        'Aplikant':'godina_rodjenja'
#    })
#)
    class Meta:
        model=Aplikant
        fields=['ime','prezime','email','godina_rodjenja','fakultet','godina_fakulteta']
        #widgets = {
        #'godina_rodjenja': forms.DateInput(format='%m/%d/%Y', input_formats=('%m/%d/%Y',), 
        #                                    attrs={'class':'Aplikant', 
        #                                'placeholder':'Unesi godinu rodjenja'})
        #}
class Prethodna_iskustva(ModelForm):
    class Meta:
        model=Aplikant
        fields=['drzanje_govora_iskustvo','opis_drzanje_govora_iskustvo','dizajn_iskustvo','opis_dizajn_iskustvo','nvo_iskustvo','opis_nvo_iskustvo']
class Dokumentacija(ModelForm):
    class Meta:
        model=Aplikant
        fields=['slika','cv','motivaciono_pismo']





