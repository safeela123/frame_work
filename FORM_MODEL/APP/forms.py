from django import forms
from .models import students

class model_form(forms.ModelForm):
    class Meta: 
        model=students
        fields='__all__'