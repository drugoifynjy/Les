from django import forms
from .models import *


class AddPassport(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'


class AddResidenceAddress(forms.ModelForm):
    class Meta:
        model = ResidenceAddress
        fields = '__all__'


class AddPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number',]
