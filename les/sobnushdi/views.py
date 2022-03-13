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
                  ("AddPlot", AddPlot),
                  ("AddPlotWoodSpecies", AddPlotWoodSpecies),
                  ]


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statements_list.html'
    context_object_name = 'statements'
    paginate_by = 10
    persons = Person.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        #person = self.persons.get(context.get('id'))
        context['title'] = 'Заявления'
        #context['person'] = person
        return context


class StatementMod(View):
    template_name = 'sobnushdi/statement_mod.html'

    def get(self, request, pk, *args, **kwargs):
        stat = get_object_or_404(Statement, pk=pk)
        date = str(stat.date)
        form_add_statement = AddStatement(initial={'date': date}, instance=stat)
        form_add_heated_promise = AddHeatedPromise(instance=stat.heated_promise)
        person = stat.person
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'pk': pk,
                'person': person,
                'title': 'Добавить заявление'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        stat = get_object_or_404(Statement, pk=pk)
        person = stat.person
        heated_promise = stat.heated_promise
        form_add_statement = ModStatement(request.POST, instance=stat)
        form_add_heated_promise = AddHeatedPromise(request.POST, instance=stat.heated_promise)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() and form_add_heated_promise.is_valid():
            heated_promise.save()
            person.save()
            stat.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class StatementAdd(CreateView):
    template_name = 'sobnushdi/statement_add.html'

    def get(self, request, pk, *args, **kwargs):
        today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
        form_add_statement = AddStatement(initial={'date': today})
        person = get_object_or_404(Person, pk=pk)
        form_add_heated_promise = AddHeatedPromise(instance=person.residence_address)
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
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() \
                and form_add_heated_promise.is_valid():
            if form_add_statement.cleaned_data['address_address']:
                addres_propisky = person.residence_address
            heated_promise = form_add_heated_promise.save()
            statement = form_add_statement.save(commit=False)
            person.save()
            statement.heated_promise = heated_promise
            statement.person = person
            statement.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ContractAdd(CreateView):
    template_name = 'sobnushdi/contract_add.html'

    def get(self, request, pk, *args, **kwargs):
        # print(request.GET)
        today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
        statement = Statement.objects.get(pk=pk)
        form_add_contract = AddContract(initial={'date': today, 'date_decree': today})
        form_add_plot = AddPlot()
        form_add_plot_wood_species = AddPlotWoodSpecies()
        form = {'form_add_contract': form_add_contract,
                'form_add_plot': form_add_plot,
                'pk': pk,
                'statement': statement,
                'title': 'Добавить договор'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        statement = get_object_or_404(Statement, pk=pk)
        form_add_contract = AddContract(request.POST, statement=statement)
        form_add_plot = AddPlot()
        print(statement)
        # print(request.POST)
        form = {'form_add_contract': form_add_contract,
                'form_add_plot': form_add_plot,
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
            #print(today)
            form_add_statement = AddStatement(initial={'date': today})
            context['title'] = 'заявление'
        elif self.steps.current == 'AddContract':
            context['title'] = 'Договор'
        elif self.steps.current == 'AddPlot':
            context['title'] = 'Делянка'
        elif self.steps.current == 'AddWoodSpecies':
            context['title'] = 'Порода'
        elif self.steps.current == 'AddPlotWoodSpecies':
            context['title'] = 'Данной породы'
        return context

    def done(self, form_list, **kwargs):
        passport = form_list[2].save() # Сохраняем паспортные данные
        person_address = form_list[1].save() # Сохраняем адресс проживания
        person = form_list[0].save(commit=False) # сохраняем данные человека
        heated_premise = form_list[3].save() # сохраняем адрес отпаливаемого помещения
        statement = form_list[4].save(commit=False) # сохраняем заявление
        person.passport = passport # привязываем паспорт к данным человека
        person.residence_address = person_address # привязываем адрес проживания к данным человека
        person.save() # сохраняем связи в классе данных человека
        statement.person = person # добавляем данные человека к заявлению
        statement.address = heated_premise # добавляем адрес отапливаемого поиещения к заявлению
        statement.save() # сохраняем связи заявления данных человека и отапливаемого помещения
        contract = form_list[5].save(commit=False) # сохраняем договор
        contract.statement = statement # привязываем заявление к договору
        contract.save() # сохраняем связь заявления и договора
        plot = form_list[6].save(commit=False)
        wood_species = form_list[7].save(commit=False)
        plot_wood_species = form_list[8].save()
        plot_wood_species.wood_species = wood_species
        return redirect('contracts_list')
