from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm



# Create your models here.

class Aplikant(models.Model):
    ime=models.CharField(max_length=20)
    prezime=models.CharField(max_length=20)
    slika=models.FileField(default=None)
    email=models.EmailField(default=None)
    godina_rodjenja=models.DateField(default=None) #input_formats=['%d.%m.%Y','%d/%m/%Y'])
    fakultet=models.CharField(max_length=30, default=None)
    godina_fakulteta=models.PositiveIntegerField(default=None)
    cv=models.FileField(default=None)
    motivaciono_pismo=models.FileField(default=None)
    drzanje_govora_iskustvo=models.BooleanField(default=False)
    opis_drzanje_govora_iskustvo=models.TextField(max_length=800,default=None)
    dizajn_iskustvo=models.BooleanField(default=False)
    opis_dizajn_iskustvo=models.TextField(max_length=800,default=None)
    nvo_iskustvo=models.BooleanField(default=False)
    opis_nvo_iskustvo=models.TextField(max_length=800,default=None)

    def get_absolute_url(self):
        return reverse('hard_podaci:index')
    def __str__(self):
        return self.ime + ' ' + self.prezime

#class AplikantForma(ModelForm):
#    class Meta:
#        model=Aplikant
#        fields=['ime','prezime','godina_rodjenja']

        

   


