from users.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name' , 'email' ,'phone', 'username' , 'password1' , 'password2' , 'user_type']

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
