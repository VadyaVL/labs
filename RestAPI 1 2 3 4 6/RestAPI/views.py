from django.shortcuts import render
from forms import *

def new(request, key='ViewEncumbrance'):
    context = {}
    context['obj'] = key
    context['id'] = -1
    if key == 'ViewEncumbrance':
        context['form'] = ViewEncumbranceForm()
    elif key == 'TypeOfEncumbrance':
        context['form'] = TypeOfEncumbranceForm()
    elif key == 'TypeReg':
        context['form'] = TypeRegForm()
    elif key == 'TypeOfCurrency':
        context['form'] = TypeOfCurrencyForm()
    elif key == 'Address':
        context['form'] = AddressForm()
    elif key == 'PAddress':
        #context['form'] = AddressForm()
        pass
    elif key == 'PPerson':
        #context['form'] = AddressForm()
        pass
    elif key == 'Person':
        context['form'] = PersonForm()
    elif key == 'Encumbrance':
        context['formE'] = EncumbranceForm

        context['formE'].base_fields['WPerson'].help_text = ''
        context['formE'].base_fields['SPerson'].help_text = ''

        context['formO'] = ObjectForm
        context['formD'] = DocumentBaseForm
        context['formT'] = TermsForm
        return render(request, 'newE.html', context)

    return render(request, 'new.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)

def edit(request, i=-1):
    context = {}
    context['id'] = i
    context['formE'] = EncumbranceForm

    context['formE'].base_fields['WPerson'].help_text = ''
    context['formE'].base_fields['SPerson'].help_text = ''

    context['formO'] = ObjectForm
    context['formD'] = DocumentBaseForm
    context['formT'] = TermsForm
    return render(request, 'newE.html', context)