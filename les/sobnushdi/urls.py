from django.urls import path

from person.views import LoginUser
from .views import StatementsView, StatementMod, ContractsView, StatementWizardAdd, StatementAdd, ContractAdd, \
    ContractWizardAdd

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('statements_list/', StatementsView.as_view(), name='statements_list'),
    #path('statements_list/', ContractsView.as_view(), name='statements_list'),
    path('statement_add/<int:pk>', StatementAdd.as_view(), name='statement_add'),
    path('statement_mod/<int:pk>', StatementAdd.as_view(), name='statement_mod'),
    path('contract_add/<int:pk>', ContractAdd.as_view(), name='contract_add'),
    path('contracts_list/', ContractsView.as_view(), name='contracts_list'),
    path('statement_wizard_add', StatementWizardAdd.as_view(), name='statement_wizard_add'),
    path('contract_wizard_add', ContractWizardAdd.as_view(), name='contract_wizard_add'),
]
