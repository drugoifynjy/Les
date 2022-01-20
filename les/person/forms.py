from django import forms
from .models import *


class AddPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class AddPassport(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'


class AddResidenceAddress(forms.ModelForm):
    class Meta:
        model = ResidenceAddress
        fields = '__all__'
