from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import CustomUser, Startapper, IdeaStartapper


class Registers(ModelForm):
    class Meta:
        model = Startapper
        fields = ['bio', 'country', 'image']


class IdeaStartapperForm(ModelForm):
    class Meta:
        model = IdeaStartapper
        fields = [ 'title', 'description', 'file']