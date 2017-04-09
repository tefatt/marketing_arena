from django.db import models
    
# Create your models here.

class Novost(models.Model):
    naslov=models.CharField(max_length=30)
    datum=models.DateField()
    sadrzaj=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.naslov

class Trening(models.Model):
    naziv=models.CharField(max_length=30)
    slika=models.ImageField(upload_to='Trening_Slike')
    opis=models.TextField(max_length=500)
    dodatni_opis=models.TextField(max_length=1000, blank=True)
    #trener=models.ForeignKey(Trener)
    
    def __str__(self):
        return self.naziv
    
class Trener(models.Model):
    ime_i_prezime=models.CharField(max_length=30)
    titula=models.CharField(max_length=30)
    slika=models.ImageField(upload_to='Trener_Slike')
    biografija=models.TextField(max_length=1000, blank=True)
    trening=models.ForeignKey(Trening)
    twitter=models.CharField(max_length=16, blank=True)
    facebook=models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.ime_i_prezime

PAKETI_MOGUCI=(('g','Godišnji'),('z','Zlatni'),('s','Srebrni'),)

class Kompanija(models.Model):
    naziv=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='Kompanija_Logo')
    web_stranica=models.CharField(max_length=30, blank=True)
    twitter=models.CharField(max_length=16, blank=True)
    facebook=models.CharField(max_length=30, blank=True)
    paket=models.CharField(max_length=1, choices=PAKETI_MOGUCI, blank=True)

    def __str__(self):
        return self.naziv

class Medij(models.Model):
    naziv=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='Medij_Logo')
    web_stranica=models.CharField(max_length=30, blank=True)
    twitter=models.CharField(max_length=16, blank=True)
    facebook=models.CharField(max_length=30, blank=True)
    paket=models.CharField(max_length=1, choices=PAKETI_MOGUCI, blank=True)

    def __str__(self):
        return self.naziv


class Agenda(models.Model):
    sadrzaj=models.FileField()

    def __str__(self):
        return self.sadrzaj
    
    
class ESN_Sarajevo(models.Model):
    opis=models.TextField(max_length=10000)
    
    def __str__(self):
        return self.opis 

class Info(models.Model):
    sazetak=models.CharField(max_length=225)
    opis=models.TextField()
    datum_objave=models.DateField()

    def __str__(self):
        return self.sazetak 


#class O_projektu(models.Model):
#    stavka=models.CharField(max_length=20)
#    opis=models.TextField(max_length=2000)

#    def __str__(self):
#        return self.stavka

