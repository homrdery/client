from django import forms
from .models import dirAddr
from django.forms import HiddenInput, ChoiceField
from crispy_forms.bootstrap import Modal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden, Button, Layout, Fieldset, Field, HTML, Reset, Row, Column
import logging

APPNAME = "client"
logger = logging.getLogger(APPNAME)




class addForm(forms.ModelForm):
    action = forms.CharField(widget=forms.HiddenInput(), initial="sub", required=True)

    # mac_addr = forms.CharField(widget=forms.Select(choices=list_mac_addr))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(Modal(Field('name'), Field('mac_addr'),Field('action'), Submit("submit", "Оправить", css_class='btn btn-primery float-end'),  css_id="addForm", title='обавить новую запись'))


    class Meta:
        model = dirAddr
        fields = ('name', 'mac_addr')

class delFormAddr(forms.ModelForm):
    action = forms.CharField(widget=forms.HiddenInput(), initial="delAddr", required=True)
    id = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Modal(Field('id'),Field('mac_addr','name', readonly=True),Field('action'), Submit("delete", "Удалить", css_class='btn btn-primery float-end'),  css_id="addFormdel", title=f"""Удалить запись с именем '{self["name"].value()}?'"""))

    class Meta:
        model = dirAddr
        fields = '__all__'
class reFormAddr(forms.ModelForm):
    action = forms.CharField(widget=forms.HiddenInput(), initial="reAddr", required=True)
    id = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Modal(Field('id'),Field('mac_addr','name'),Field('action'), Submit("edit", "Изменить", css_class='btn btn-primery float-end'),  css_id="addFormdel", title=f"""Изменить запись с именем '{self["name"].value()}'?"""))

    class Meta:
        model = dirAddr
        fields = ('id','mac_addr', 'name')
