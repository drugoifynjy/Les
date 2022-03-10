from django import forms
from django.utils.datetime_safe import datetime

from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'
    value = datetime.now()


class AddStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'date']
        widgets = {
            'date': MyDateInput,
        }


class ModStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['person', 'number_statement', 'date', 'there_is_a_contract', 'refusal_to_conclude_a_contract']
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
        fields = ['decision_on_statement', 'number_decree', 'date_decree', 'number', 'date']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput,
        }


class ModContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['statement', 'decision_on_statement', 'number_decree', 'date_decree', 'number', 'date']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput,
        }


class AddPlot(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['number_plot', 'date', 'forestry', 'district_forestry', 'tract',
                  'quarter', 'section', 'chop_type', 'cost']
        widgets = {
            'date': MyDateInput,
    }


class AddWoodSpecies(forms.ModelForm):
    class Meta:
        model = WoodSpecies
        fields = ['name_wood_species', ]


class AddPlotWoodSpecies(forms.ModelForm):
    class Meta:
        model = PlotWoodSpecies
        fields = ['wood_species', 'number_of_trees', 'large', 'average', 'small',
                  'firewood', 'price']
        widgets = {
            'date': MyDateInput,
        }
