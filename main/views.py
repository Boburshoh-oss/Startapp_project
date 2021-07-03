from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import *
from .forms import *

# Create your views here.

def home (request):
    return render(request , 'main/home.html' , {})

class Startappersview(ListView):
    template_name = 'main/startapper.html'
    model = Startapper

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = StartapperForm()
        return context
    def post(self , request , *args , **kwargs):
        form = StartapperForm(request.POST , request.FILES)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('home')


class Devlopersview(ListView):
    template_name = 'main/startapper.html'
    model = Developer

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = DeveloperForm()
        return context

    def post(self , request , *args , **kwargs):
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')