from django.urls import path

from person.views import LoginUser
from .views import StatementsView, StatementAdd, StatementMod


urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('statements/', StatementsView.as_view(), name='statements'),
    path('statements_mod/<int:pk>', StatementMod.as_view(), name='statements_mod'),
    path('statements_add/', StatementAdd.as_view(), name='statements_add'),

]
