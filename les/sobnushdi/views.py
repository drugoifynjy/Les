from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView, UpdateView, View
from formtools.wizard.views import SessionWizardView
from .forms import *
from person.forms import AddPassport, AddResidenceAddress, AddPerson

FORMS_STATEMENT = [("passport", AddPassport),
                   ("AddResidenceAddress", AddResidenceAddress),
                   ("person", AddPerson),
                   ("AddHeatedPromise", AddHeatedPromise),
                   ("AddStatement", AddStatement),
                   ]


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statement_list.html'
    context_object_name = 'statements'
    paginate_by = 10

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
        today = str(datetime.now())[0:10] # Текущая дата без времени для вставки в форму ввода даты заявления
        print(today)
        form_add_statement = AddStatement(initial={'date': today})
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
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'form_select_person_in_statement': form_select_person_in_statement,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() \
                and form_add_heated_promise.is_valid() \
                and form_select_person_in_statement.is_valid():
            heated_promise = form_add_heated_promise.save()
            statement = form_add_statement.save(commit=False)
            statement.heated_promise = heated_promise
            statement.person = form_select_person_in_statement.save()
            statement.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class PersonWizardAdd(SessionWizardView):
    form_list = FORMS_STATEMENT
    template_name = 'sobnushdi/statement_wizard_add.html'

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        if self.steps.current == 'passport':
            context['title'] = 'данные пасспорта'
        elif self.steps.current == 'AddResidenceAddress':
            context['title'] = 'прописка'
        elif self.steps.current == 'person':
            context['title'] = 'заявитель'
        elif self.steps.current == 'AddHeatedPromise':
            context['title'] = 'адрес отапливаемого помещения'
        elif self.steps.current == 'AddStatement':
            context['title'] = 'заявление'
        return context

    def done(self, form_list, **kwargs):
        if form_list[0].is_valid and form_list[1].is_valid and form_list[2].is_valid:
            passport = form_list[0].save()
            person_address = form_list[1].save()
            person = form_list[2].save(commit=False)
            heated_premise = form_list[3].save()
            statement = form_list[4].save(commit=False)
            person.passport = passport
            person.residence_address = person_address
            person.save()
            statement.person = person
            statement.address = heated_premise
            statement.save()
            return redirect('statements_list')


class ContractsView(ListView):
    model = Contract
    template_name = 'sobnushdi/contracts_list.html'
    context_object_name = 'contracts'
    fields = ['statement', 'number_decree', 'date_decree', 'number', 'date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Договора'
        return context
