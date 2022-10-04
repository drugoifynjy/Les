from django import forms
from django.utils.datetime_safe import datetime

from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'
    value = datetime.now()


class AddStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'quantity', 'date']
        widgets = {
            'date': MyDateInput,
        }


class ModStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'date', 'quantity', ]
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
        fields = ['number_decree', 'date_decree', 'number', 'date',
                  'the_end_date_of_the_export_of_wood', 'end_date_of_wood_harvesting']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput, 'end_date_of_wood_harvesting':MyDateInput,
            'the_end_date_of_the_export_of_wood': MyDateInput,
        }


class ModContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['number_decree', 'date_decree', 'number', 'date',
                  'the_end_date_of_the_export_of_wood', 'end_date_of_wood_harvesting', 'plot']
        widgets = {
            'date': MyDateInput, 'date_decree': MyDateInput, 'the_end_date_of_the_export_of_wood':MyDateInput,
            'end_date_of_wood_harvesting':MyDateInput
        }


class AddPlot(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['number_plot', 'tract', 'area',
                  'quarter', 'section', 'chop_type', 'cost', 'cost_in_words']
        widgets = {
            'cost': forms.TextInput(attrs={'readonly': True}),
        }


class AddPlotWoodSpecies(forms.ModelForm):
    class Meta:
        model = PlotWoodSpecies
        fields = ['name', 'number_of_trees', 'large', 'average', 'small',
                  'firewood', 'brushwood', 'price']
        widgets = {
            'date': MyDateInput,
        }


class AddBreed(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name', ]


class AddTract(forms.ModelForm):
    class Meta:
        model = Tract
        fields = ['name', ]


# class AddForestry(forms.ModelForm):
#     class Meta:
#         model = Forestry
#         fields = ['name', ]


class AddDistrictForestry(forms.ModelForm):
    class Meta:
        model = DistrictForestry
        fields = ['name', 'forestry']

