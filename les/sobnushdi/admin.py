from django.contrib import admin

from .models import *


@admin.register(HeatedPremise)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('locality', 'street', 'house_number', 'apartment_number')


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ('number_statement', 'date')
    list_filter = ('date',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'date')
    list_filter = ('date',)


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('number_plot', 'forestry', 'district_forestry', 'tract',
                    'quarter', 'section', 'chop_type', 'cost')
    #list_filter = ('date',)


@admin.register(PlotWoodSpecies)
class PlotWoodSpeciesAdmin(admin.ModelAdmin):
    list_display = ('number_of_trees', 'large', 'average', 'small', 'firewood', 'price')
    #list_filter = ('date',)


@admin.register(Breeds)
class BreedsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #list_filter = ('date',)
