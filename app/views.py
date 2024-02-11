from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.forms import *
# Create your views here.

class templatehtml(TemplateView):
    template_name='templatehtml.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='prameela'
        ECDO['age']=23
        return ECDO
    


class insertschooltempview(templatehtml):
    template_name='insertschooltempview.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['SFO']=schoolForm
        return ECDO
    
    def post(self,request):
        SFDO=schoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('it is vallid') 
        




class insertschoolbyformview(FormView):
    template_name='insertschoolbyformview.html'
    form_class=schoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('insertschoolbyformview is done')