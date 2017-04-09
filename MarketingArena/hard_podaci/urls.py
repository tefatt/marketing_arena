from django.conf.urls import url
from hard_podaci import views

app_name='hard_podaci'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^kompanije', views.prikaz_kompanija, name='prikaz_kompanija'),
    url(r'^medij', views.prikaz_medija, name='prikaz_medija'),
    url(r'^novost', views.prikaz_novosti, name='prikaz_novosti'),
    url(r'^trener', views.prikaz_trenera, name='prikaz_trenera'),
    url(r'^trening', views.prikaz_treninga, name='prikaz_treninga'),
    url(r'^ESN Sarajevo', views.prikaz_ESN_Sa, name='prikaz_ESN_Sa'),
    url(r'^agenda', views.prikaz_agenda, name='prikaz_agenda'),
    url(r'^kontakt', views.kontakt_forma, name='kontakt_forma')
    ]