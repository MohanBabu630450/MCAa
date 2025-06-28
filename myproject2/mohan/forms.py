from django import forms
from .models import Faculity

class FaculityForm(forms.ModelForm):
    class Meta:
        model = Faculity
        fields = ['name', 'email', 'department']

# Create your tests here.
