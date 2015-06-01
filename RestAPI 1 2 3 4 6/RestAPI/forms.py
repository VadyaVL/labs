from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from models import *

class ViewEncumbranceForm(ModelForm):

    class Meta:
        model = ViewEncumbrance

        #widgets = {'Text': forms.Textarea(attrs={'cols': 5, 'rows': 5})}

class TypeOfEncumbranceForm(ModelForm):

    class Meta:
        model = TypeOfEncumbrance

class TypeRegForm(ModelForm):

    class Meta:
        model = TypeReg

class TypeOfCurrencyForm(ModelForm):

    class Meta:
        model = TypeOfCurrency

class AddressForm(ModelForm):

    class Meta:
        model = Address

class PersonForm(ModelForm):

    class Meta:
        model = Person

########################################

class EncumbranceForm(ModelForm):

    class Meta:
        model = Encumbrance
        fields = ['NStatement',
                  'DateStatement',
                  'TypeOfEncumbrance',
                  'TypeReg',
                  'ViewEncumbrance',
                  'Date',
                  'AddedInfo',
                  'WPerson',
                  'SPerson']

class ObjectForm(ModelForm):

    class Meta:
        model = Object
        fields = ['Name','SerialNumber','RegNumber','AddedInfoForUNMovable',]

class DocumentBaseForm(ModelForm):

    class Meta:
        model = DocumentBase
        fields = ['Name','Number','Date','PublisherName',]

class TermsForm(ModelForm):

    class Meta:
        model = Terms
        fields = ['SizeObligations','LimitDate','AddedInfo','TypeOfCurrency',]