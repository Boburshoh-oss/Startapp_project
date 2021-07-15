from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .forms import Register
# Create your views here.

def index(request):
    return render (request , 'users/base.html' ,{})

@login_required(login_url='login')
def startapper(request):
    return render(request , 'users/startapper.html' , {})


@login_required(login_url='login')
def developer(request):
    return render(request, 'users/developer.html', {})

@login_required(login_url='login')
def practitioner(request):
    return render(request, 'users/practitioner.html', {})
    
    
        