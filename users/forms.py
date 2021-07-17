from django.forms import ModelForm
from django import forms
from .models import AllUsersIdea , ApplicationStaff

from .models import CustomUser, Startapper, IdeaStartapper


class Registers(ModelForm):
    class Meta:
        model = Startapper
        fields = ['bio', 'country', 'image']


class IdeaStartapperForm(ModelForm):
    class Meta:
        model = IdeaStartapper
        fields = [ 'title', 'description', 'file']


class AllIdeas(forms.ModelForm):
    class Meta:
        model = AllUsersIdea
        fields = ['title' , 'description' , 'file']

class Applications(forms.ModelForm):
    class Meta:
        model = ApplicationStaff
        fields = ['title' , 'description' , 'resume' , 'work_type']
