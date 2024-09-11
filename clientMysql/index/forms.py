from django import forms
from .models import worker
import crispy_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden, Button, Layout, Fieldset, Field, HTML, Reset, Row, Column


class addForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

    class Meta:
        model = worker
        fields = ('name', 'mac_addr')

