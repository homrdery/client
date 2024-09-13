from django import forms
from .models import worker
from django.forms import HiddenInput
import crispy_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden, Button, Layout, Fieldset, Field, HTML, Reset, Row, Column


class addForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/Addr/addpost/'
        self.helper.add_input(Submit('submit', 'Отправить', css_class='btn btn-primary float-end'))
        self.helper.layout = Layout(Fieldset('name', 'mac_addr'))
        self.fields['mac_addr'].widget = HiddenInput()


    class Meta:
        model = worker
        fields = ('name', 'mac_addr')


