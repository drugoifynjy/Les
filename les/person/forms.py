from django import forms
from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'


class MyPhoneNumber(forms.NumberInput):
    max_length = 11


class AddPassport(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ['series', 'number', 'date_of_issue', 'issued', 'address_birth', 'inn']
        widgets = {
            'address_birth': forms.TextInput,
            'date_of_issue': MyDateInput,
        }


class AddResidenceAddress(forms.ModelForm):
    class Meta:
        model = ResidenceAddress
        fields = '__all__'


class AddPerson(forms.ModelForm):
    name = 'Паспорт'
    class Meta:
        model = Person
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number']
        widgets = {
            'date_of_bird': MyDateInput,
        }

