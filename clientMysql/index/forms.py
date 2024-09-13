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
        self.helper.form_action = '/Addr/addPost/'
        self.helper.add_input(Submit('submit', 'Отправить', css_class='btn btn-primary float-end'))

    class Meta:
        model = worker
        fields = ('name')


