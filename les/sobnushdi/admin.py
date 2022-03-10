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


@admin.register(Plot)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract', 'number_plot', 'date', 'forestry', 'district_forestry', 'tract',
                    'quarter', 'section', 'chop_type', 'cost')
    #list_filter = ('date',)


@admin.register(WoodSpecies)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('plot', 'name_wood_species')
    #list_filter = ('date',)


@admin.register(PlotWoodSpecies)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('wood_species', 'number_of_trees', 'large', 'average', 'small', 'firewood', 'price')
    #list_filter = ('date',)


@admin.register(Breeds)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #list_filter = ('date',)
