from django.urls import path

from person.views import LoginUser
from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('statements_list/', StatementsView.as_view(), name='statements_list'),
    path('statements/statement_add/<int:pk>', StatementAdd.as_view(), name='statement_add'),
    path('statements/statement_mod/<int:pk>', StatementMod.as_view(), name='statement_mod'),

    path('contracts/contracts_list/', ContractsView.as_view(), name='contracts_list'),
    path('contracts/contract_add/<int:pk>', ContractAdd.as_view(), name='contract_add'),
    path('contracts/contract_mod/<int:pk>', ContractMod.as_view(), name='contract_mod'),
    path('contracts/contract_print/<int:pk>', ContractPrint.as_view(), name='contract_print'),
    path('contracts/contract_view/<int:pk>', ContractView.as_view(), name='contract_view'),
    path('contracts/contract/<int:pk>', Contract.as_view(), name='contract'),

    path('plot_wood_species/plot_wood_species_add/<int:pk>', PlotWoodSpeciesAdd.as_view(), name='plot_wood_species_add'),
    path('plot_wood_species/plot_wood_species_mod/<int:pk>', PlotWoodSpeciesMod.as_view(), name='plot_wood_species_mod'),

    path('guides/', GuidesView.as_view(), name='guides'),

    path('guides/breeds/', BreedsView.as_view(), name='breeds'),
    path('guides/breeds/breed_mod/<int:pk>', BreedMod.as_view(), name='breed_mod'),
    path('guides/breeds/form_del/<int:pk>', BreedDel.as_view(), name='form_breed_del'),

    path('guides/tracts/', TractsView.as_view(), name='tracts'),
    path('guides/tracts/tract_mod/<int:pk>', TractMod.as_view(), name='tract_mod'),
    path('guides/tracts/form_del/<int:pk>', TractDel.as_view(), name='form_tract_del'),

    path('guides/forestrys/', ForestryView.as_view(), name='forestrys'),
    path('guides/forestrys/forestry_mod/<int:pk>', ForestryMod.as_view(), name='forestry_mod'),
    path('guides/forestrys/form_del/<int:pk>', ForestryDel.as_view(), name='form_forestry_del'),

    path('guides/district_forestrys/', DistrictForestryView.as_view(), name='district_forestrys'),
    path('guides/district_forestrys/district_forestry_mod/<int:pk>', DistrictForestryMod.as_view(), name='district_forestry_mod'),
    path('guides/district_forestrys/form_del/<int:pk>', DistrictForestryDel.as_view(), name='form_district_forestry_del'),
]
