from django import forms
from django.utils.datetime_safe import datetime

from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'
    value = datetime.now()


class AddStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'quantity', 'date', 'address_address', ]
        widgets = {
            'date': MyDateInput,
        }


class ModStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'date', 'quantity', 'refusal_to_conclude_a_contract', ]
        widgets = {
            'date': MyDateInput,
        }


class AddHeatedPromise(forms.ModelForm):
    class Meta:
        model = HeatedPremise
        fields = '__all__'


class AddContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['number_decree', 'date_decree', 'number', 'date']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput,
        }


class ModContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['number_decree', 'date_decree', 'number', 'date', 'plot']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput,
        }


class AddPlot(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['number_plot', 'forestry', 'district_forestry', 'tract',
                  'quarter', 'section', 'chop_type', 'cost']
        widgets = {
            'date': MyDateInput,
    }


class AddPlotWoodSpecies(forms.ModelForm):
    class Meta:
        model = PlotWoodSpecies
        fields = ['number_of_trees', 'large', 'average', 'small',
                  'firewood', 'price']
        widgets = {
            'date': MyDateInput,
        }


class AddBreeds(forms.ModelForm):
    class Meta:
        model = Breeds
        fields = ['name', ]


class AddTract(forms.ModelForm):
    class Meta:
        model = Tract
        fields = ['name', ]
