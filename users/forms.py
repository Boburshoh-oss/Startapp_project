from django import forms
from .models import AllUsersIdea , ApplicationStaff

class AllIdeas(forms.ModelForm):
    class Meta:
        model = AllUsersIdea
        fields = ['title' , 'description' , 'file']

class Applications(forms.ModelForm):
    class Meta:
        model = ApplicationStaff
        fields = ['title' , 'description' , 'resume' , 'work_type']
