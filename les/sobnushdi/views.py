from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View, DeleteView, DetailView
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


class GuidesView(View):
    template_names = 'sobnushdi/guides/guides.html'

    def get(self, request, *args, **kwargs):
        form = {
            'title': 'Справочники'
        }
        return render(request, self.template_names, context=form)


class ForestryView(ListView):
    model = Forestry
    template_name = 'sobnushdi/guides/forestrys.html'
    context_object_name = 'forestrys'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        gg = self.model.objects.all()
        print(gg)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Лесничества'
        return context


class ForestryMod(CreateView):
    template_name = 'sobnushdi/guides/forestry_mod.html'
    paginate_by = 10

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            forestry = Forestry.objects.get(pk=pk)
            form_mod_forestry = AddForestry(instance=forestry)
        else:
            form_mod_forestry = AddForestry()
        form = {'form_mod_forestry': form_mod_forestry,
                'pk': pk,
                'title': 'Добавить лесничество'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            forestry = Forestry.objects.get(pk=pk)
            form_mod_forestry = AddForestry(request.POST, instance=forestry)
        else:
            form_mod_forestry = AddForestry(request.POST)
        form = {'form_mod_forestry': form_mod_forestry,
                'title': 'Добавить лесничество'}
        if form_mod_forestry.is_valid():
            if pk:
                forestry.save()
            else:
                form_mod_forestry.save()
            return redirect('forestrys')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ForestryDel(DeleteView):
    template_name = 'sobnushdi/guides/form_del.html'
    model = Forestry
    success_url = reverse_lazy('forestrys')


class TractsView(ListView):
    model = Tract
    template_name = 'sobnushdi/guides/tracts.html'
    context_object_name = 'tracts'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Урочища'
        return context


class TractMod(CreateView):
    template_name = 'sobnushdi/guides/tract_mod.html'
    paginate_by = 10

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            tract = Tract.objects.get(pk=pk)
            form_mod_tract = AddTract(instance=tract)
        else:
            form_mod_tract = AddTract()
        form = {'form_mod_tract': form_mod_tract,
                'pk': pk,
                'title': 'Добавить породу'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            tract = Tract.objects.get(pk=pk)
            form_mod_tract = AddTract(request.POST, instance=tract)
        else:
            form_mod_tract = AddTract(request.POST)
        form = {'form_mod_tract': form_mod_tract,
                'title': 'Добавить породу'}
        if form_mod_tract.is_valid():
            if pk:
                tract.save()
            else:
                form_mod_tract.save()
            return redirect('tracts')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class TractDel(DeleteView):
    template_name = 'sobnushdi/guides/form_del.html'
    model = Tract
    success_url = reverse_lazy('tracts')


class BreedsView(ListView):
    model = Breed
    template_name = 'sobnushdi/guides/breeds.html'
    context_object_name = 'breeds'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Породы'
        return context


class BreedMod(CreateView):
    template_name = 'sobnushdi/guides/breed_mod.html'
    paginate_by = 10

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            breed = Breed.objects.get(pk=pk)
            form_mod_breed = AddBreed(instance=breed)
        else:
            form_mod_breed = AddBreed()
        form = {'form_mod_breed': form_mod_breed,
                'pk': pk,
                'title': 'Порода'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            breed = Breed.objects.get(pk=pk)
            form_mod_breed = AddBreed(request.POST, instance=breed)
        else:
            form_mod_breed = AddBreed(request.POST)
        form = {'form_mod_breed': form_mod_breed,
                'title': 'Порода'}
        if form_mod_breed.is_valid():
            if pk:
                breed.save()
            else:
                form_mod_breed.save()
            return redirect('breeds')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class BreedDel(DeleteView):
    template_name = 'sobnushdi/guides/form_del.html'
    model = Breed
    success_url = reverse_lazy('breeds')


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statements/statements_list.html'
    context_object_name = 'statements'
    paginate_by = 10
    #persons = Person.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementAdd(CreateView):
    template_name = 'sobnushdi/statements/statement_add.html'

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


class StatementMod(View):
    template_name = 'sobnushdi/statements/statement_mod.html'

    def get(self, request, pk, *args, **kwargs):
        stat = get_object_or_404(Statement, pk=pk)
        date = str(stat.date)
        form_add_statement = AddStatement(initial={'date': date}, instance=stat)
        form_add_heated_promise = AddHeatedPromise(instance=stat.heated_promise)
        person = stat.person
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
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


class StatementDel(DeleteView):
    template_name = 'sobnushdi/form_del.html'
    model = Statement
    success_url = reverse_lazy('breeds')


class ContractsView(ListView):
    model = Contract
    template_name = 'sobnushdi/contracts/contracts_list.html'
    context_object_name = 'contracts'
    fields = ['statement', 'number_decree', 'date_decree', 'number', 'date']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        for contract in Contract.objects.all():
            plot = contract.plot
            plot_wood_specie = plot.plot_wood_species.all()
            plot.cost = 0
            for i in plot_wood_specie:
                print(i.price)
                plot.cost += float(i.price)
            print(plot.cost)
            plot.save()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Договора'
        return context


class ContractAdd(CreateView):
    template_name = 'sobnushdi/contracts/contract_add.html'

    def get(self, request, pk, *args, **kwargs):
        # print(request.GET)
        today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
        statement = Statement.objects.get(pk=pk)
        form_add_contract = AddContract(initial={'date': today, 'date_decree': today, 'statement': statement})
        form_add_plot = AddPlot()
        form = {'person': statement.person,
                'form_add_contract': form_add_contract,
                'form_add_plot': form_add_plot,
                'pk': pk,
                'statement': statement,
                'title': 'Добавить договор'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        statement = get_object_or_404(Statement, pk=pk)
        form_add_contract = AddContract(request.POST)
        form_add_plot = AddPlot(request.POST)
        form = {'form_add_contract': form_add_contract,
                'form_add_plot': form_add_plot,
                'statement': statement,
                'title': 'Добавить договор'}
        if form_add_contract.is_valid():
            plot = form_add_plot.save()
            contract = form_add_contract.save(commit=False)
            contract.statement = statement
            contract.plot = plot
            contract.save()
            return redirect('contracts_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ContractMod(CreateView):
    template_name = 'sobnushdi/contracts/contract_mod.html'

    def get(self, request, pk, *args, **kwargs):
        # print(request.GET)
        contract = Contract.objects.get(pk=pk)
        date = str(contract.date)
        date_decree = str(contract.date_decree)
        statement = contract.statement
        plot = contract.plot
        form_add_contract = AddContract(initial={'date': date, 'date_decree': date_decree}, instance=contract)
        form_add_plot = AddPlot(instance=plot)
        form = {'person': statement.person,
                'form_add_contract': form_add_contract,
                'form_add_plot': form_add_plot,
                'pk': pk,
                'statement': statement,
                'title': 'Добавить договор'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        statement = contract.statement
        plot = contract.plot
        form_add_contract = AddContract(request.POST, instance=contract)
        form_add_plot = AddPlot(request.POST, instance=plot)
        form = {'person': statement.person,
                'form_add_contract': form_add_contract,
                'form_add_plot': form_add_plot,
                'pk': pk,
                'statement': statement,
                'title': 'Добавить договор'}
        if form_add_contract.is_valid() and form_add_plot.is_valid():
            form_add_contract.save(commit=False)
            form_add_plot.save()
            form_add_contract.save()
            return redirect('contracts_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ContractView(View):
    template_name = 'sobnushdi/contracts/contract_view.html'

    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        date = str(contract.date)
        person = contract.statement.person
        plot = contract.plot
        plot_wood_species = contract.plot.plot_wood_species.all()
        form = {'contract': contract,
                'date': date,
                'person': person,
                'plot': plot,
                'plot_wood_species': plot_wood_species,
                'title': 'Данные договора'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        contract = get_object_or_404(Contract, pk=pk)
        date = str(contract.date)
        person = contract.statement.person
        plot = contract.plot
        plot_wood_species = contract.plot.plot_wood_species.all()
        for i in plot_wood_species:
            print(i.name, i.number_of_trees)
        form = {'contract': contract,
                'date': date,
                'person': person,
                'plot_wood_species': plot_wood_species,
                'title': 'Данные договора'}
        for plot_wood_specie in plot_wood_species:
            if plot_wood_specie.is_valid():
                plot_wood_specie.save()
        plot.save()
        contract.save()
        return redirect('contracts_list')
        return render(request, self.template_name, context=form)


class PlotWoodSpeciesAdd(CreateView):
    template_name = 'sobnushdi/plot_wood_species/plot_wood_species_add.html'

    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        plot = contract.plot
        form_add_plot_wood_species = AddPlotWoodSpecies(initial={'plot': plot})
        form = {'person': contract.statement.person,
                'contract': contract,
                'plot': plot,
                'pk': pk,
                'form_add_plot_wood_species': form_add_plot_wood_species,
                'title': 'Добавить данные по породе в деляне к договору' + str(contract.number)}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        plot = contract.plot
        form_add_plot_wood_species = AddPlotWoodSpecies(request.POST)
        form = {'person': contract.statement.person,
                'contract': contract,
                'plot': plot,
                'pk': pk,
                'form_add_plot_wood_species': form_add_plot_wood_species,
                'title': 'Добавить данные по породе в деляне к договору' + str(contract.number)}
        if form_add_plot_wood_species.is_valid():
            plot_wood_species = form_add_plot_wood_species.save()
            plot.cost += float(plot_wood_species.price)
            plot.plot_wood_species.add(plot_wood_species)
            plot.save()
            return redirect('contracts_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class PlotWoodSpeciesMod(CreateView):
    template_name = 'sobnushdi/plot_wood_species/plot_wood_species_mod.html'
    beck = ''

    def get(self, request, pk=None, *args, **kwargs):
        plot_wood_species = PlotWoodSpecies.objects.get(pk=pk)
        plot = Plot.objects.get(plot_wood_species=plot_wood_species)
        contract = Contract.objects.get(plot=plot)
        person = contract.statement.person
        #print(plot)
        form_mod_plot_wood_species = AddPlotWoodSpecies(instance=plot_wood_species)
        form = {
            'person': person,
            'contract': contract,
            'plot': plot,
            'pk': pk,
            'form_mod_plot_wood_species': form_mod_plot_wood_species,
            'title': 'contract.number'}
        self.beck = request.META['HTTP_REFERER']
        print(self.beck)
        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        plot_wood_species = PlotWoodSpecies.objects.get(pk=pk)
        plot = Plot.objects.get(plot_wood_species=plot_wood_species)
        form_mod_plot_wood_species = AddPlotWoodSpecies(request.POST, instance=plot_wood_species)
        contract = Contract.objects.get(plot=plot)
        person = contract.statement.person
        form = {
            'person': person,
            'contract': contract,
            'plot': plot,
            'pk': pk,
            'form_add_plot_wood_species': form_mod_plot_wood_species,
            'title': 'contract.number'}
        if form_mod_plot_wood_species.is_valid():
            plot_wood_species.save()
            return redirect('contracts_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


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
