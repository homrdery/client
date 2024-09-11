from django import forms
from .models import worker
import crispy_forms

class addForm(forms.ModelForm):


    class Meta:
        model = worker
        fields = ('name', 'mac_addr')

