from django.contrib import admin
from hard_podaci.models import *
# Register your models here.

class NovostAdmin(admin.ModelAdmin):
    list_display=('naslov','datum',)
    search_fields=['naslov','datum']
    list_filter=('naslov','datum',)


class TreningAdmin(admin.ModelAdmin):
    list_display=('naziv',)
    search_fields=['naziv']
    list_filter=('trener__ime_i_prezime','naziv',)
    fieldsets= (
        ('Osnovno', { "fields": ('naziv','slika','opis',)}),
        ('Dodatno', {"classes":("collapse",),
                          "fields":("dodatni_opis",),
                          "description": "Dodaj dodatni opis"}) 
        )

class TrenerAdmin(admin.ModelAdmin):
    list_display=('ime_i_prezime','trening',)
    search_fields=['ime_i_prezime','trening']
    list_filter=('trening__naziv','ime_i_prezime','titula',)
    fieldsets= (
        ('Osnovni podaci', { "fields": ('ime_i_prezime','titula','slika','biografija','trening',)}),
        ('Društvene mreže', {"classes":("collapse",),
                          "fields":("twitter","facebook",),
                          "description": "Dodaj društvene mreže ovdje"}) 
        )

class KompanijaAdmin(admin.ModelAdmin):
    list_display=('naziv','paket',)
    search_fields=['naziv','paket']
    list_filter=('naziv','paket',)
    fieldsets= (
        ('Osnovni podaci', { "fields": ('naziv','logo','paket',)}),
        ('Kontakt podaci', {"classes":("collapse",),
                          "fields":("web_stranica","twitter","facebook",),
                          "description": "Dodaj kontake ovdje"}) 
        )

class MedijAdmin(admin.ModelAdmin):
    list_display=('naziv','paket',)
    search_fields=['naziv','paket']
    list_filter=('naziv','paket',)
    fieldsets= (
        ('Osnovni podaci', { "fields": ('naziv','logo','paket',)}),
        ('Kontakt podaci', {"classes":("collapse",),
                          "fields":("web_stranica","twitter","facebook",),
                          "description": "Dodaj kontake ovdje"}) 
        )
class AgendaAdmin(admin.ModelAdmin):
    list_display=('sadrzaj',)

class ESN_SaAdmin(admin.ModelAdmin):
    list_display=('opis',)

class Info_Admin(admin.ModelAdmin):
    list_display=('sazetak','opis','datum_objave',)


admin.site.register(Novost,NovostAdmin)

admin.site.register(Trening,TreningAdmin)

admin.site.register(Trener,TrenerAdmin)

admin.site.register(Kompanija,KompanijaAdmin)

admin.site.register(Medij,MedijAdmin)

admin.site.register(Agenda,AgendaAdmin)

admin.site.register(ESN_Sarajevo,ESN_SaAdmin)

admin.site.register(Info,Info_Admin)

