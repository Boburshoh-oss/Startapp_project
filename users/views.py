from django.contrib import messages
from users.models import ApplicationStaff, Staff, Startapper , IdeaStartapper , AllUsersIdea 
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .forms import AllIdeas , Applications
from django.utils.datastructures import MultiValueDictKeyError
# from .forms import Register
# Create your views here.
from users.forms import Registers , IdeaStartapperForm
from users.models import Startapper , IdeaStartapper


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
    try:
        user = Staff.objects.get(user = request.user)
    except:
        messages.warning(request , 'You are in developers page you are not developer')
        return redirect('users:index')

    developers = Staff.objects.filter(user__user_type = user.user.user_type)

    if request.method == 'POST':
        form = Applications(request.POST , request.FILES)
        if form.is_valid():
            data = ApplicationStaff()
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            try:
                data.resume = request.FILES['resume']
            except MultiValueDictKeyError:
                messages.warning(request, 'Resume required')
                return redirect('users:Developer')
            data.work_type = form.cleaned_data['work_type']
            data.user = user
            data.save()
            messages.success(request, 'You application successfully send')
            return redirect('users:profile')
        else:
            messages.warning(request, 'Application not send!')
            return redirect('users:Developer')

    applicationform = Applications() 

    context = {
        'developers':developers,
        'applicationform':applicationform
    }
    return render(request, 'users/developer.html', context)

@login_required(login_url='login')
def practitioner(request):
    return render(request, 'users/practitioner.html', {})
    
def profile_page(request):
    if request.user.user_type == "Startapper":
        user = Startapper.objects.get(user = request.user)
        ideas = IdeaStartapper.objects.filter(user = user)
        application = None
    else:
        user = Staff.objects.get(user = request.user)
        ideas = AllUsersIdea.objects.filter(user = request.user)
        try:
            application = ApplicationStaff.objects.get(user = user)
        except:
            application = None   
    if request.method == 'POST':
        form = AllIdeas(request.POST , request.FILES)
        if form.is_valid():
            data = AllUsersIdea()
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            data.file = request.FILES['file']
            data.user = request.user
            data.save()
            messages.success(request, 'Successfully idea send!')
            return redirect('users:profile')
        else:
            messages.warning(request , 'An error accured please sendagain!!')
            return redirect('users:profile')
    else:
        form = AllIdeas()
    context = { 'user':user ,
              'ideas' :ideas ,
        'application' : application,
        'ideaform': form
        }
    return render(request , 'users/profile.html' , context)
    

class StaffUpdateWiew(UpdateView):
    model = Staff
    fields = ['bio' , 'country' , 'image']
    template_name = 'users/update.html'

    def get_success_url(self):
        return '/profile'

class StartapperUpdateWiew(UpdateView):
    model = Startapper
    fields = ['bio' , 'country' , 'image']
    template_name = 'users/update.html'

    def get_success_url(self):
        return '/profile'

class AppUpdateWiew(UpdateView):
    model = ApplicationStaff
    fields = ['title' , 'description' , 'work_type' , 'resume']
    template_name = 'users/update.html'

    def get_success_url(self):
        return '/profile'
