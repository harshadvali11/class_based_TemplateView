from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.forms import *
class RenderHtml(TemplateView):
    template_name='RenderHtml.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Ashu'
        ECDO['age']=5
        ECDO['ESFO']=SchoolForm()
        return ECDO

    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted')


class SchoolFV(FormView):
    template_name='SchoolFV.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('Done')



