from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, View


from .forms import *
from person.views import PersonAdd


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statement_list.html'
    context_object_name = 'statements'
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementMod(View):
    model = Statement
    template_name = 'sobnushdi/statement_mod.html'
    context_object_name = 'statement_mod'
    fields = ['number_statement', 'date', 'address']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementAdd(CreateView):
    template_name = 'sobnushdi/statement_add.html'

    def get(self, request, *args, **kwargs):
        form_add_statement = AddStatement()
        form_add_heated_promise = AddHeatedPromise()
        form_select_person_in_statement = SelectPersonInStatement()
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'form_select_person_in_statement': form_select_person_in_statement,
                'title': 'Добавить заявление'}
        return render(request, self.template_name, context=form)

    def post(self, request, *args, **kwargs):
        form_add_statement = AddStatement(request.POST)
        form_add_heated_promise = AddHeatedPromise(request.POST)
        form_select_person_in_statement = SelectPersonInStatement(request.POST)
        form = CreateManufacturerForm(initial={'createddate': datetime.now()})
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'form_select_person_in_statement': form_select_person_in_statement,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() and form_add_heated_promise.is_valid() and form_select_person_in_statement.is_valid():
            heated_promise = form_add_heated_promise.save()
            statement = form_add_statement.save(commit=False)
            statement.heated_promise = heated_promise
            statement.person = form_select_person_in_statement.save()
            statement.save()
            return request.META['HTTP_REFERER']

        return render(request, self.template_name, context=form)






class ContractsView(ListView):
    model = Contract
    template_name = 'sobnushdi/contracts_list.html'
    context_object_name = 'contracts'
    fields = ['statement', 'number_decree', 'date_decree', 'number', 'date']
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Договора'
        return context
