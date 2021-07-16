from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import CustomUser, Startapper


class Registers(ModelForm):
    class Meta:
        model = Startapper
        fields = ['bio', 'country', 'image']