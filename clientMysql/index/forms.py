from django import forms
from .models import worker, Pktreader
from django.forms import HiddenInput, ChoiceField
from crispy_forms.bootstrap import Modal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden, Button, Layout, Fieldset, Field, HTML, Reset, Row, Column


def list_mac_addr():
    box = Pktreader.objects.all().order_by('mac_addr').values_list('mac_addr', flat=True)
    return box
class addForm(forms.ModelForm):
    action = forms.CharField(widget=forms.HiddenInput(), initial="sub", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(Modal(Field('name'), Field('mac_addr'),Field('action'), Submit("submit", "Оправить", css_class='btn btn-primery float-end'),  css_id="addForm", title='РАботаееет'))
        self.fields['mac_addr'].widget = ChoiceField(choices=list_mac_addr)


    class Meta:
        model = worker
        fields = ('name', 'mac_addr')


# class addFormAddr(forms.ModelForm):
#     action = forms.CharField(widget=forms.HiddenInput(), initial="sub", required=True)
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_action = ''
#         self.helper.layout = Layout(Modal(Field('name', 'mac_addr', select='mac_addr' 'action'), Submit("submit", "Оправить", css_class='btn btn-primery float-end'),  css_id="addForm", title='РАботаееет'))
#         self.fields['mac_addr'].widget = HiddenInput()
#
