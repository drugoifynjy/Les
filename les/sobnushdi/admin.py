from django.contrib import admin

from .models import *


@admin.register(HeatedPremise)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('locality', 'street', 'house_number', 'apartment_number')


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ('number_statement', 'date', 'person')
    list_filter = ('date',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = ('number', 'date', 'statement')
    list_filter = ('date',)
