from django import forms
from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'


class MyPhoneNumber(forms.NumberInput):
    max_length = 11


class AddPassport(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'
        widgets = {
            'date_of_issue': MyDateInput,
        }


class UpdatePassport(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'
        widgets = {
            'address_birth': forms.TextInput,
        }


class AddResidenceAddress(forms.ModelForm):
    class Meta:
        model = ResidenceAddress
        fields = '__all__'


class AddPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number']
        widgets = {
            'date_of_bird': MyDateInput,
        }


class UpdatePerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number']
