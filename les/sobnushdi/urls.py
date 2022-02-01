from django.urls import path

from person.views import LoginUser
from .views import StatementsView, StatementAdd, StatementMod, ContractsView


urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('statements_list/', StatementsView.as_view(), name='statements_list'),
    path('statement_mod/<int:pk>', StatementMod.as_view(), name='statement_mod'),
    path('statement_add/', StatementAdd.as_view(), name='statement_add'),
    path('contracts_list/', ContractsView.as_view(), name='contracts_list'),
]
