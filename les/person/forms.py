from django import forms
from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'


class AddLocalityType(forms.ModelForm):
    class Meta:
        model = LocalityType
        fields = '__all__'


class AddPersonPassport(forms.ModelForm):
    prefix = 'person_passport'
    class Meta:
        model = PersonPassport
        fields = ['series', 'number', 'date_of_issue', 'issued', 'address_birth', 'inn']
        labels = {'series': 'person_series', 'number': 'person_number'}
        widgets = {'date_of_issue': MyDateInput, }


class AddRepresentativePassport(forms.ModelForm):
    prefix = 'representative_passport'
    class Meta:
        model = RepresentativePassport
        fields = ['series', 'number', 'date_of_issue', 'issued', 'address_birth', 'inn']
        widgets = {'date_of_issue': MyDateInput, }


class AddPersonResidenceAddress(forms.ModelForm):
    prefix = 'person_residence_address'
    class Meta:
        model = PersonResidenceAddress
        fields = '__all__'


class AddRepresentativeResidenceAddress(forms.ModelForm):
    prefix = 'representative_residence_address'
    class Meta:
        model = RepresentativeResidenceAddress
        fields = '__all__'


class AddPerson(forms.ModelForm):
    prefix = 'person'
    class Meta:
        model = Person
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number',
                  'there_is_a_representative']
        widgets = {
            'date_of_bird': MyDateInput,
        }


class AddRepresentativePerson(forms.ModelForm):
    prefix = 'representative'
    class Meta:
        model = RepresentativePerson
        fields = ['second_name', 'first_name', 'patronymic', 'date_of_bird', 'phone_number']
        widgets = {
            'date_of_bird': MyDateInput,
        }

