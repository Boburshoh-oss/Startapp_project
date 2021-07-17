from django.shortcuts import redirect, render
from .forms import Register , Login
from django.contrib.auth import login , authenticate
from users.models import Startapper , Staff

# Create your views here.

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            print(user.user_type,"..............................")
            if user:
                login(request , user)
                startapper = Startapper()
                staff= Staff()
                
                if user.user_type == 'Startapper':
                    startapper.user = user
                    startapper.save()
                elif user.user_type:
                    staff.user = user
                    staff.save()
                return redirect(f'users:{user.user_type}')

    else:
        form = Register()
    return render(request, 'register/registration.html', {'form':form})
    
def log_in(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request=request , username = username , password= password)
            if user:
                login(request,user)
                if user.user_type:
                    return redirect(f'users:{user.user_type}')
                else:
                    return redirect('users:index')
    else:
        form = Login()
    return render(request , 'register/login.html' , {'form':form})

