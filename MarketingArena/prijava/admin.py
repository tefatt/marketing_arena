from django.contrib import admin
from prijava.models import *

# Register your models here.

class AplikantAdmin(admin.ModelAdmin):
    list_display=('ime','prezime',)
    search_fields=['ime','prezime','godina_rodjenja']
    list_filter=('ime','prezime','godina_rodjenja',)
admin.site.register(Aplikant, AplikantAdmin)