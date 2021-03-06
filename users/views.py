from django.contrib import messages
from users.models import ApplicationStaff, Staff, Startapper , IdeaStartapper , AllUsersIdea, SuccessProjects , CommentOfPost
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .forms import AllIdeas , Applications , IdeaStartapper , Comments , IdeaStartapperForm
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseRedirect
# from .forms import Register
# Create your views here.



def index(request):
    return render (request , 'users/base.html' ,{})

@login_required(login_url='login')
def startapper(request):
    try:
        user = Startapper.objects.get(user = request.user)
    except:
        messages.warning(request , 'You are in practitioners page you are not developer')
        return redirect('users:index')
    ideas = IdeaStartapper.objects.all()
    startappers = Startapper.objects.all()
    context = {
        'ideas':ideas,
        'startappers':startappers
    }
    return render(request , 'users/startapper.html' , context)

def ideastartapper(request):
    form = IdeaStartapperForm()
    startappr = Startapper.objects.get(user=request.user)
    idea = IdeaStartapper()
    if request.method == "POST":
        form = IdeaStartapperForm(request.POST, request.FILES)
        if form.is_valid():
            idea.user = startappr
            idea.title =  form.cleaned_data['title']
            idea.description = form.cleaned_data['description']
            idea.file = request.FILES['file']
            idea.save()
            return redirect("users:Startapper")
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
    try:
        user = Staff.objects.get(user = request.user)
    except:
        messages.warning(request , 'You are in practitioners page you are not developer')
        return redirect('users:index')

    practitioner = Staff.objects.filter(user__user_type = user.user.user_type)

    if request.method == 'POST':
        form = Applications(request.POST , request.FILES)
        if form.is_valid():
            data = ApplicationStaff()
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            try:
                data.resume = request.FILES['resume']
            except MultiValueDictKeyError:
                data.resume = None
            data.work_type = form.cleaned_data['work_type']
            data.user = user
            data.save()
            messages.success(request, 'You application successfully send')
            return redirect('users:profile')
        else:
            messages.warning(request, 'Application not send!')
            return redirect('users:Practitioners')

    applicationform = Applications() 

    context = {
        'practitioner':practitioner,
        'applicationform':applicationform
    }
    return render(request, 'users/practitioner.html', context)    
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

def successProject(request):
    project = SuccessProjects.objects.all()
    return render(request, 'users/successProjects.html' , {'project':project})
    
def projectDetatils(request , pk):
    project = SuccessProjects.objects.get(pk=pk)
    comment = CommentOfPost.objects.filter(post_id=pk)
    return render(request, 'users/projectDetails.html', {'project': project, 'comment': comment})

def comments(request, pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comments(request.POST)
        if form.is_valid():
            data = CommentOfPost()
            data.comment = form.cleaned_data['comment']
            data.post_id = pk
            current_user = request.user
            data.owner_id = current_user.id
            data.save()
            messages.success(request, 'Your comment successfully send!')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


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
