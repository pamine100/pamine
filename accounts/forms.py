from PIL import Image, ImageFilter

from django import forms
from django.forms import modelformset_factory, DateTimeField, BaseModelFormSet

from django.core.exceptions import ValidationError
from django.contrib.admin import widgets

from accounts.models import PersonAccount

ACCOUNT_TYPE_CHOICES = (
    ('Buyer', 'Buyer'),
    ('Seller', 'Seller'),
)
def isEmptyOrSingleChar(data,isText):
    if data == None or str(data) == 'None':
        return True
    elif len(str(data)) < 2 and isText:
        return True
    else:
        return False


class AccountForm(forms.ModelForm):
    error_css_class = 'error'
    
    def __init__(self, *args, **kwargs):
        self._pk=kwargs.pop('id', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = PersonAccount
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Email','maxlength':70,'class':'input-box'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password','maxlength':50,'class':'input-box'}),
            'first_name': forms.TextInput(attrs={'placeholder':'First Name','maxlength':256,'class':'input-box'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name','maxlength':256,'class':'input-box'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone Number(11 digits)','maxlength':11,'class':'input-box'}),
            'address': forms.TextInput(attrs={'placeholder':'Address','maxlength':256,'class':'input-box'}),
        }