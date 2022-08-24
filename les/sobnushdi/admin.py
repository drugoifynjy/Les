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
    list_display = ('number_plot', 'forestry', 'district_forestry', 'tract', 'area',
                    'quarter', 'section', 'chop_type', 'cost')


@admin.register(PlotWoodSpecies)
class PlotWoodSpeciesAdmin(admin.ModelAdmin):
    list_display = ('number_of_trees', 'large', 'average', 'small', 'firewood', 'price')


@admin.register(Breed)
class BreedsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tract)
class TractAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DistrictForestry)
class DistrictForestryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Forestry)
class ForestryAdmin(admin.ModelAdmin):
    list_display = ('name',)
