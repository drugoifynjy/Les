from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView

from .models import *


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statement_list.html'
    context_object_name = 'statements'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementMod(UpdateView):
    model = Statement
    template_name = 'sobnushdi/statement_mod.html'
    context_object_name = 'statements'
    fields = ['number_statement', 'date', 'address']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementAdd(CreateView):
    model = Statement
    template_name = 'sobnushdi/statement_add.html'
    fields = ['number_statement', 'date', 'address', 'person']
