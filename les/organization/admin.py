from django.contrib import admin

from .models import *


@admin.register(OrganizationAddress)
class OrganizationAddressAdmin(admin.ModelAdmin):
    list_display = ('locality', 'street', 'house_number', 'apartment_number')


@admin.register(RequisitesOrganization)
class RequisitesOrganizationAdmin(admin.ModelAdmin):
    list_display = ('INN', 'KPP', 'OGRN', 'OKPO', 'email')


@admin.register(BankDetails)
class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ('bank_title', 'bank_account', 'correspondent_account', 'BIK', 'organization')


@admin.register(DepartmentRepresentative)
class DepartmentRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name', 'patronymic', 'position', 'department')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization_address', 'requisites_organization')


@admin.register(PowerOfAttorneyRepresentative)
class PowerOfAttorneyRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('number', 'start_date', 'end_date', 'organization_representative', 'selected')
