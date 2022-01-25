from django.urls import path

from person.views import LoginUser
from . import views

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('statements/', views.StatementView.as_view(), name='statements'),

]
