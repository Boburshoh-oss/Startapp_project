from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import Register
# Create your views here.
from users.forms import Registers
from users.models import Startapper


def index(request):
    return render (request , 'users/base.html' ,{})

@login_required(login_url='login')
def startapper(request):
    return render(request , 'users/startapper.html' , {})

def detail(request):
    form = Registers()
    startappr = Startapper.objects.get(user=request.user)
    if request.method == "POST":
        form = Registers(request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            country = form.cleaned_data['country']
            image = request.FILES['image']
            startappr.bio = bio
            startappr.country = country
            startappr.image = image
            startappr.save()
            redirect("/")
    return render(request, 'uses/detail.html', {'form': form})        

def ideastartapper(request):
    form = IdeaStartapperForm()
    startappr = Startapper.objects.get(user=request.user)
    idea = IdeaStartapper.objects.get(user=startappr)
    if request.method == "POST":
        form = IdeaStartapperForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = request.FILES['file']
            idea.title = title
            idea.description = description
            idea.file = file
            idea.save()
            redirect("Startapper/")
    return render(request, 'users/ideastartapper.html', {'form': form})

@login_required(login_url='login')
def developer(request):
    return render(request, 'users/developer.html', {})

@login_required(login_url='login')
def practitioner(request):
    return render(request, 'users/practitioner.html', {})
    
    
def detail(request):
    form = Registers()
    startappr = Startapper.objects.get(user=request.user)
    if request.method == "POST":
        form = Registers(request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            country = form.cleaned_data['country']
            image = request.FILES['image']
            startappr.bio = bio
            startappr.country = country
            startappr.image = image
            startappr.save()
            redirect("/")
    return render(request, 'uses/detail.html', {'form': form})        