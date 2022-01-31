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
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementMod(UpdateView):
    model = Statement
    template_name = 'sobnushdi/statement_mod.html'
    context_object_name = 'statement_mod'
    fields = ['number_statement', 'date', 'address']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementAdd(CreateView):
    model = Statement
    context_object_name = 'statement_add'
    template_name = 'sobnushdi/statement_add.html'
    fields = ['number_statement', 'date', 'address', 'person']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить заявление'
        return context


class ContractsView(ListView):
    model = Contract
    template_name = 'sobnushdi/contract_list.html'
    context_object_name = 'contracts'
    fields = ['statement', 'number_decree', 'date_decree', 'number', 'date']
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Договора'
        return context
