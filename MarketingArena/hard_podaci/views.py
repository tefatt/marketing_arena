from django.shortcuts import render, redirect
from hard_podaci.models import *
from django import forms
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

 


# Create your views here.

def index(request):
    return render(request, 'hard_podaci/index.html')

def prikaz_kompanija(request):
    sve_komp= Kompanija.objects.all()
    srebrni=[]
    zlatni=[]
    godisnji=[]
    for komp in sve_komp:
        if komp.paket=='g':
            godisnji.append(komp)
        elif komp.paket=='z':
            zlatni.append(komp)
        elif komp.paket=='s':
            srebrni.append(komp)
    return render(request, 'hard_podaci/kompanije.html', {'godisnji':godisnji, 'zlatni': zlatni, 'srebrni':srebrni})

def prikaz_medija(request):
    svi_mediji= Medij.objects.all()
    #srebrni,zlatni,godisnji=zip([],[],[])
    srebrni=[]
    zlatni=[]
    godisnji=[]
    for medij in svi_mediji:
        if medij.paket=='g':
            godisnji.append(medij)
        elif medij.paket=='z':
            zlatni.append(medij)
        elif medij.paket=='s':
            srebrni.append(medij)
    return render(request, 'hard_podaci/mediji.html', {'godisnji':godisnji, 'zlatni': zlatni, 'srebrni':srebrni})

def prikaz_novosti(request):
    sve_novosti= Novost.objects.all()
    paginator = Paginator(sve_novosti, 3) 
    page = request.GET.get('page')

    try:
        novosti = paginator.page(page)
    except PageNotAnInteger:
        novosti = paginator.page(1)
    except EmptyPage:
        novosti = paginator.page(paginator.num_pages)

    return render(request, 'hard_podaci/novosti.html', {'novosti':novosti})

def prikaz_trenera(request):
    svi_treneri= Trener.objects.all()
    return render(request, 'hard_podaci/trener.html',{'treneri': svi_treneri})

def prikaz_treninga(request):
    svi_treninzi= Trening.objects.all()
    return render(request, 'hard_podaci/treninzi.html',{'treninzi': svi_treninzi})

def prikaz_ESN_Sa(request):
    ESN= Trening.objects.all()
    return render(request, 'hard_podaci/ESN_Sarajevo.html',{'ESN': ESN})

def prikaz_agenda(request):
    agenda= Trening.objects.all()
    return render(request, 'hard_podaci/agenda.html',{'agenda': agenda})

class ContactForm(forms.Form):
    kontakt_ime=forms.CharField(required=True)
    kontakt_email = forms.EmailField(required=True)
    sadrzaj = forms.CharField(required=True,widget=forms.Textarea)

def kontakt_forma(request):
    forma=ContactForm
    if request.method=='POST':
        form=forma(data=request.POST)
        if form.is_valid():
            kontakt_ime=request.POST.get('kontakt_ime','')
            kontakt_email=request.POST.get('kontakt_email','')
            sadrzaj=request.POST.get('sadrzaj','')

            template=get_template('kontakt_template.txt')
            context = Context({
                'kontakt_ime': kontakt_ime,
                'kontakt_email': kontakt_email,
                'sadrzaj': sadrzaj,
            })
            content=template.render(context)
            email=EmailMessage(
                "Imate novu email poruku",
                content,
                "www.Marketing Arena.ba ",
                ['ens@gmail.com'],
                headers={'Odgovorite':kontakt_email }
                )
            email.send()
            return redirect('hard_podaci:index')
    return render(request,'hard_podaci/kontakt_forma.html', {'forma':forma})
     