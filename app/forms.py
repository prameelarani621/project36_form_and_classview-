from django import forms
from app.models import *
class schoolForm(forms.ModelForm):
    class Meta():
        model=school
        fields='__all__'