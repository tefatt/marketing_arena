from django.shortcuts import render, render_to_response
from prijava.models import Aplikant
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.checks.security import csrf
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from formtools.wizard.views import SessionWizardView


class PrijavaWizard(SessionWizardView):
    template_name='prijava/form_aplikant.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'aplikant_files'))
    #def get_form_instance( self, step ):
    #    if self.instance is None:
    #        self.instance = Aplikant()
    #    return self.instance
    def done(self, form_list, **kwargs):
                
        ap=Aplikant()
        items=[]
        fields=[['ime','prezime','email','godina_rodjenja','fakultet','godina_fakulteta'],
                ['drzanje_govora_iskustvo','opis_drzanje_govora_iskustvo','dizajn_iskustvo','opis_dizajn_iskustvo','nvo_iskustvo','opis_nvo_iskustvo'],
                ['slika','cv','motivaciono_pismo']]
        for form in form_list:
            items.append((form.cleaned_data.items()))
        for i in range(len(fields)):
            for x,y in items[i]:
                setattr(ap,x,y)
        ap.save()
        return render(self.request, 'prijava/done.html',
                      {'form_data': [form.cleaned_data for form in form_list],}
                      )




#class UpdateAplikanta(UpdateView):
#    model=Aplikant
#    fields=['ime','prezime','godina_rodjenja']

#class BrisanjeAplikanta(DeleteView):
#    model=Aplikant
#    success_url=reverse_lazy('prijava:index')

#def create(request):
#    if request.POST:
#        form=AplikantForma(request.POST)
#        if form.is_valid():
#            form.save()

#            return HttpResponseRedirect('prijava.html')
#    else:
#        form=AplikantForma()

#    args={}
#    args.update(csrf(request))
#    args['form']=form

#    return render_to_response('aplikant_form.html', args)

#class IndexView(generic.ListView):
#    template_name='prijava/prijava.html'

#    def get_queryset(self):
#        return Aplikant.objects.all()

#class DetailView(generic.DetailView):
#    model=Aplikant
#    template_name='prijava/detail.html'

#def DetailView(request):
#    return render(request,'prijava/detail.html')