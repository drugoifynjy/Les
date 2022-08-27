from django import forms
from django.utils.datetime_safe import datetime

from .models import *


class AddOrganization(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['title']


class AddOrganizationAddress(forms.ModelForm):
    class Meta:
        model = OrganizationAddress
        fields = '__all__'


class AddRequisitesOrganization(forms.ModelForm):
    class Meta:
        model = RequisitesOrganization
        fields = ['INN', 'KPP', 'OGRN', 'OKPO', 'email']


class AddBankDetals(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = '__all__'


class AddOrModRepresentativeOrganization(forms.ModelForm):
    class Meta:
        model = OrganizationRepresentative
        fields = ['second_name', 'first_name', 'patronymic', 'position', 'organization']
