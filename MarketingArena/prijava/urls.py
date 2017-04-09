from django.conf.urls import url
from prijava import views
from prijava.forms import *


#url= site/prijava/
app_name='prijava'

urlpatterns=[
    url(r'^', views.PrijavaWizard.as_view([Opsti_podaci, Dokumentacija, Prethodna_iskustva]), name='unos_aplikanta'),
    #url(r'^prijavljeni$', views.IndexView.as_view(), name='index'),
    #url(r'^detail', views.DetailView, name='detail'),
    #url(r'^(?P<pk>[0-9]+)/', views.UpdateView.as_view(), name='update'),
    #url(r'^(?P<pk>[0-9]+)/izbrisi/', views.DeleteView.as_view(), name='delete'),


    ]