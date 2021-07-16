from users.models import Staff, Startapper , IdeaStartapper , AllUsersIdea
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
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
    
def profile_page(request):
    if request.user.user_type == "Startapper":
        user = Startapper.objects.get(user = request.user)
        ideas = IdeaStartapper.objects.filter(user = user)
    else:
        user = Staff.objects.get(user = request.user)
        ideas = AllUsersIdea.objects.filter(user = request.user)
    return render(request , 'users/profile.html' , { 'user':user , 'ideas' :ideas })
    
class StaffUpdateWiew(UpdateView):
    model = Staff
    fields = ['bio' , 'country' , 'image']
    template_name = 'users/update.html'

    def get_success_url(self):
        return redirect('users:profile')
    # success_url = 'users:profile'