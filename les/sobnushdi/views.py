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
from person.models import Person

FORMS_STATEMENT = [("person", AddPerson),
                   ("AddResidenceAddress", AddResidenceAddress),
                   ("passport", AddPassport),
                   ("AddHeatedPromise", AddHeatedPromise),
                   ("AddStatement", AddStatement),
                  ]

FORMS_CONTRACT = [("person", AddPerson),
                 ("AddResidenceAddress", AddResidenceAddress),
                 ("passport", AddPassport),
                 ("AddHeatedPromise", AddHeatedPromise),
                 ("AddStatement", AddStatement),
                 ("AddContract", AddContract),
                ]


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statements_list.html'
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

    def get(self, request, pk, *args, **kwargs):
        #print(request.GET)
        today = str(datetime.now())[0:10] # Текущая дата без времени для вставки в форму ввода даты заявления
        #print(today)
        form_add_statement = AddStatement(initial={'date': today})
        form_add_heated_promise = AddHeatedPromise()
        person = get_object_or_404(Person, pk=pk)
        print(person)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'pk': pk,
                'person': person,
                'title': 'Добавить заявление'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        form_add_statement = AddStatement(request.POST)
        form_add_heated_promise = AddHeatedPromise(request.POST)
        person = get_object_or_404(Person, pk=pk)
        print(person.first_name)
        #print(request.POST)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() \
                and form_add_heated_promise.is_valid():
            heated_promise = form_add_heated_promise.save()
            statement = form_add_statement.save(commit=False)
            statement.heated_promise = heated_promise
            statement.person = Person.objects.get(pk=pk)
            statement.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ContractAdd(CreateView):
    template_name = 'sobnushdi/contract_add.html'

    def get(self, request, pk, *args, **kwargs):
        #print(request.GET)
        today = str(datetime.now())[0:10] # Текущая дата без времени для вставки в форму ввода даты заявления
        #print(today)
        form_add_contract = AddContract(initial={'date': today, 'date_decree': today})

        statement = get_object_or_404(Statement, pk=pk)
        print(statement)
        form = {'form_add_contract': form_add_contract,
                'pk': pk,
                'statement': statement,
                'title': 'Добавить договор'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        form_add_contract = AddContract(request.POST)
        statement = get_object_or_404(Statement, pk=pk)
        print(statement)
        #print(request.POST)
        form = {'form_add_contract': form_add_contract,
                'statement': statement,
                'title': 'Добавить договор'}
        if form_add_contract.is_valid():
            contract = form_add_contract.save(commit=False)
            contract.statement = Statement.objects.get(pk=pk)
            contract.save()
            return redirect('contracts_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ContractsView(ListView):
    model = Contract
    template_name = 'sobnushdi/contracts_list.html'
    context_object_name = 'contracts'
    fields = ['statement', 'number_decree', 'date_decree', 'number', 'date']
    paginate_by = 10
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Договора'
        return context


class StatementWizardAdd(SessionWizardView):
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
            today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
            print(today)
            form_add_statement = AddStatement(initial={'date': today})
            context['title'] = 'заявление'
        return context

    def done(self, form_list, **kwargs):
            passport = form_list[2].save()
            person_address = form_list[1].save()
            person = form_list[0].save(commit=False)
            heated_premise = form_list[3].save()
            statement = form_list[4].save(commit=False)
            person.passport = passport
            person.residence_address = person_address
            person.save()
            statement.person = person
            statement.address = heated_premise
            statement.save()
            return redirect('statements_list')


class ContractWizardAdd(SessionWizardView):
    form_list = FORMS_CONTRACT
    template_name = 'sobnushdi/contract_wizard_add.html'

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
            today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
            print(today)
            form_add_statement = AddStatement(initial={'date': today})
            context['title'] = 'заявление'
        elif self.steps.current == 'AddContract':
            context['title'] = 'Договор'
        return context

    def done(self, form_list, **kwargs):
            passport = form_list[2].save()
            person_address = form_list[1].save()
            person = form_list[0].save(commit=False)
            heated_premise = form_list[3].save()
            statement = form_list[4].save(commit=False)
            person.passport = passport
            person.residence_address = person_address
            person.save()
            statement.person = person
            statement.address = heated_premise
            statement.save()
            contract = form_list[5].save(commit=False)
            contract.statement = statement
            contract.save()
            return redirect('contracts_list')
