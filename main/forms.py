from django import forms
from .models import Startapper,Developer

class StartapperForm(forms.ModelForm):
    class Meta:
        model = Startapper
        fields = ('name', 'video','audio','pdf','document','description' )
        
class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('name', 'last_name','image','age','description','email','phone' )