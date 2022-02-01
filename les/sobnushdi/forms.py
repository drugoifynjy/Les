from django import forms
from .models import *


class AddStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['number_statement', 'date']


class SelectPersonInStatement(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['person']


class AddHeatedPromise(forms.ModelForm):
    class Meta:
        model = HeatedPremise
        fields = '__all__'


class AddContract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
