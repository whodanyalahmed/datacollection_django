from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from .models import personal_data
# Create your views here.


class Home(ListView): 
    template_name = "index.html"
    model = personal_data
    context_object_name = 'name'

class update(UpdateView):
    template_name = 'edit.html'
    model = personal_data
    fields = ['name','fathername','age','ph','address']
    success_url = '/'

