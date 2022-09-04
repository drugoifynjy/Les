from django import forms
from django.utils.datetime_safe import datetime

from .models import *


class AddOrganization(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['title', 'selected']


class AddOrganizationAddress(forms.ModelForm):
    class Meta:
        model = OrganizationAddress
        fields = '__all__'


class AddRequisitesOrganization(forms.ModelForm):
    class Meta:
        model = RequisitesOrganization
        fields = ['INN', 'KPP', 'OGRN', 'OKPO', 'email']


class AddOrModBankDetals(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ['bank_title', 'bank_account', 'correspondent_account', 'BIK', 'selected']


class AddOrModRepresentativeOrganization(forms.ModelForm):
    class Meta:
        model = OrganizationRepresentative
        fields = ['second_name', 'first_name', 'patronymic', 'position', 'selected']
