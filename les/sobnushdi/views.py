from openpyxl import load_workbook
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View, DeleteView
from datetime import timedelta
from .forms import *

from person.models import Person
from organization.models import *

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
    ordering = '-pk'
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


class DistrictForestryView(ListView):
    model = DistrictForestry
    template_name = 'sobnushdi/guides/district_forestrys.html'
    context_object_name = 'district_forestrys'
    paginate_by = 10
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        gg = self.model.objects.all()
        print(gg)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Участковые лесничества'
        return context


class DistrictForestryMod(CreateView):
    template_name = 'sobnushdi/guides/district_forestry_mod.html'
    paginate_by = 10

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            district_forestry = DistrictForestry.objects.get(pk=pk)
            form_mod_district_forestry = AddDistrictForestry(instance=district_forestry)
        else:
            form_mod_district_forestry = AddDistrictForestry()
        form = {'form_mod_district_forestry': form_mod_district_forestry,
                'pk': pk,
                'title': 'Добавить участковое лесничество'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            district_forestry = DistrictForestry.objects.get(pk=pk)
            form_mod_district_forestry = AddDistrictForestry(request.POST, instance=district_forestry)
        else:
            form_mod_district_forestry = AddDistrictForestry(request.POST)
        form = {'form_mod_district_forestry': form_mod_district_forestry,
                'title': 'Добавить участковое лесничество'}
        if form_mod_district_forestry.is_valid():
            if pk:
                district_forestry.save()
            else:
                form_mod_district_forestry.save()
            return redirect('district_forestrys')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class DistrictForestryDel(DeleteView):
    template_name = 'sobnushdi/guides/form_del.html'
    model = DistrictForestry
    success_url = reverse_lazy('district_forestrys')


class TractsView(ListView):
    model = Tract
    template_name = 'sobnushdi/guides/tracts.html'
    context_object_name = 'tracts'
    paginate_by = 10
    ordering = '-pk'

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
    ordering = '-pk'

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
    ordering = '-pk'

    # persons = Person.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        for statement in self.object_list:
            statement.date = statement.date.strftime("%d.%m.%Y")
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementAdd(CreateView):
    template_name = 'sobnushdi/statements/statement_add.html'

    def get(self, request, pk, *args, **kwargs):
        today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
        form_add_statement = AddStatement(initial={'date': today})
        person = Person.objects.get(pk=pk)
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
        person = Person.objects.get(pk=pk)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() \
                and form_add_heated_promise.is_valid():
            heated_promise = form_add_heated_promise.save()
            statement = form_add_statement.save(commit=False)
            statement.organization = Organization.objects.get(selected=True)
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
        stat = Statement.objects.get(pk=pk)
        date = str(stat.date)
        form_add_statement = AddStatement(initial={'date': date}, instance=stat)
        form_add_heated_promise = AddHeatedPromise(instance=stat.heated_promise)
        person = stat.person
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'pk': pk,
                'title': 'Добавить заявление'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        stat = Statement.objects.get(pk=pk)
        person = stat.person
        heated_promise = stat.heated_promise
        form_add_statement = ModStatement(request.POST, instance=stat)
        form_add_heated_promise = AddHeatedPromise(request.POST, instance=stat.heated_promise)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'pk': pk,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() and form_add_heated_promise.is_valid():
            stat.organization = Organization.objects.get(selected=True)
            heated_promise.save()
            person.save()
            stat.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class ContractsView(ListView):
    model = Contract
    template_name = 'sobnushdi/contracts/contracts_list.html'
    context_object_name = 'contracts'
    fields = ['statement', 'number_decree', 'date_decree', 'number', 'date']
    paginate_by = 10
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        for contract in self.object_list:
            contract.date = contract.date.strftime("%d.%m.%Y")
            contract.statement.date = contract.statement.date.strftime("%d.%m.%Y")
            plot_wood_speciess = contract.plot.plot_wood_species.all()
            contract.plot.cost = 0
            for i in plot_wood_speciess:
                contract.plot.cost += i.price
                #print(i.price)
            contract.plot.save()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Договора'
        return context


class ContractAdd(CreateView):
    template_name = 'sobnushdi/contracts/contract_add.html'

    def get(self, request, pk, *args, **kwargs):
        statement = Statement.objects.get(pk=pk)
        date1 = statement.date + timedelta(14)
        date2 = statement.date + timedelta(45)
        end_date = date2 + timedelta(364)
        # my_birthday = my_birthday.replace(year=today.year + 1)
        #print(statement.date, ' ', date1, ' ', date2)
        form_add_contract = AddContract(initial={'date': str(date2), 'date_decree': str(date1),
                                                 'statement': statement,
                                                 'the_end_date_of_the_export_of_wood': str(end_date),
                                                 'end_date_of_wood_harvesting': str(end_date),
                                                 })
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
        end_date = str(contract.end_date_of_wood_harvesting)
        statement = contract.statement
        plot = contract.plot
        form_add_contract = AddContract(initial={'date': date, 'date_decree': date_decree,
                                                 'the_end_date_of_the_export_of_wood': end_date,
                                                 'end_date_of_wood_harvesting': end_date
                                                 }, instance=contract)
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
        plot.cost = 0
        plot.business = 0
        plot.firewood = 0
        plot.brushwood = 0
        plot.liquid_wood = 0
        plot.total = 0
        for plot_wood_specie in plot_wood_species:
            plot.cost += plot_wood_specie.price
            plot.business += plot_wood_specie.large + plot_wood_specie.average + plot_wood_specie.small
            plot.firewood += plot_wood_specie.firewood
            plot.brushwood += plot_wood_specie.brushwood
        plot.liquid_wood += plot.business + plot.firewood
        plot.total = plot.liquid_wood + plot.brushwood
        form = {'contract': contract,
                'date': date,
                'person': person,
                'plot': plot,
                'plot_wood_species': plot_wood_species,
                'title': 'Данные договора'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        date_contract = str(contract.date)
        person = contract.statement.person
        plot = contract.plot
        plot_wood_species = contract.plot.plot_wood_species.all()
        form = {'contract': contract,
                'date': date_contract,
                'person': person,
                'plot_wood_species': plot_wood_species,
                'title': 'Данные договора'}
        for plot_wood_specie in plot_wood_species:
            if plot_wood_specie.is_valid():
                plot_wood_specie.save()
            plot.plot_wood_species.add(plot_wood_specie)
        plot.save()
        contract.save()
        return render(request, self.template_name, context=form)


class ContractPrint(View):
    template_name = 'sobnushdi/contracts/contract_print.html'
    file_name = "sobnushdi/templates/for_print/contract.xlsx"
    work_book = load_workbook(file_name)
    page = work_book['Договор']

    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        self.page['BP2'] = contract.number
        self.page['BP3'] = contract.date
        self.page['BP4'] = contract.date+timedelta(days=364)
        self.page['BP5'] = contract.date+timedelta(days=364)
        self.page['BP7'] = contract.date_decree
        self.page['BP8'] = contract.number_decree

        self.page['BP10'] = str(contract.statement.person)
        self.page['BP11'] = contract.statement.person.passport.series
        self.page['BP12'] = contract.statement.person.passport.number
        self.page['BP13'] = contract.statement.person.passport.date_of_issue
        self.page['BP14'] = contract.statement.person.passport.issued

        self.page['BP20'] = contract.statement.person.passport.address_birth
        self.page['BP21'] = contract.statement.person.date_of_bird
        self.page['BP22'] = contract.statement.person.passport.address_birth
        self.page['BP23'] = contract.statement.person.passport.inn
        self.page['BP24'] = str(contract.statement.person.residence_address)

        self.page['BP43'] = contract.plot.area
        self.page['BP44'] = contract.plot.district_forestry.name
        self.page['BP45'] = contract.plot.tract.name
        self.page['BP46'] = contract.plot.quarter
        self.page['BP47'] = contract.plot.section
        self.page['BP48'] = contract.plot.number_plot

        self.page['BP57'] = contract.plot.chop_type
        self.page['BP62'] = contract.plot.cost
        if contract.plot.plot_wood_species.filter(name__name='Береза'):
            birch = contract.plot.plot_wood_species.filter(name__name='Береза')
        else:
            birch = False
        if contract.plot.plot_wood_species.filter(name__name='Осина'):
            aspen = contract.plot.plot_wood_species.filter(name__name='Осина')
        else:
            aspen = False
        if birch:
            self.page['BP84'] = birch[0].number_of_trees
            self.page['BP85'] = birch[0].large
            self.page['BP86'] = birch[0].average
            self.page['BP87'] = birch[0].small
            self.page['BP88'] = birch[0].firewood
            self.page['BP89'] = birch[0].brushwood

        if aspen:
            self.page['BP94'] = aspen[0].number_of_trees
            self.page['BP95'] = aspen[0].large
            self.page['BP96'] = aspen[0].average
            self.page['BP97'] = aspen[0].small
            self.page['BP98'] = aspen[0].firewood
            self.page['BP99'] = aspen[0].brushwood

        self.work_book.save('Договор ' + str(contract.statement.person) + '.xlsx')
        self.work_book.close()
        return redirect('contracts_list')


class ContractVee(View):
    template_name = 'sobnushdi/contracts/contract.html'

    def get(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        organ = Organization.objects.get(selected=True)
        bank_detail = organ.bankdetails_set.get(selected=True)
        organ_repr = organ.organizationrepresentative_set.get(selected=True)
        print(organ_repr, bank_detail)
        '''contract.number
        self.page['BP3'] = contract.date
        self.page['BP4'] = contract.date + timedelta(days=364)
        self.page['BP5'] = contract.date + timedelta(days=364)
        self.page['BP7'] = contract.date_decree
        self.page['BP8'] = contract.number_decree

        self.page['BP10'] = str(contract.statement.person)
        self.page['BP11'] = contract.statement.person.passport.series
        self.page['BP12'] = contract.statement.person.passport.number
        self.page['BP13'] = contract.statement.person.passport.date_of_issue
        self.page['BP14'] = contract.statement.person.passport.issued

        self.page['BP20'] = contract.statement.person.passport.address_birth
        self.page['BP21'] = contract.statement.person.date_of_bird
        self.page['BP22'] = contract.statement.person.passport.address_birth
        self.page['BP23'] = contract.statement.person.passport.inn
        self.page['BP24'] = str(contract.statement.person.residence_address)

        self.page['BP43'] = contract.plot.area
        self.page['BP44'] = contract.plot.district_forestry.name
        self.page['BP45'] = contract.plot.tract.name
        self.page['BP46'] = contract.plot.quarter
        self.page['BP47'] = contract.plot.section
        self.page['BP48'] = contract.plot.number_plot

        self.page['BP57'] = contract.plot.chop_type
        self.page['BP62'] = contract.plot.cost
        if contract.plot.plot_wood_species.filter(name__name='Береза'):
            birch = contract.plot.plot_wood_species.filter(name__name='Береза')
        else:
            birch = False
        if contract.plot.plot_wood_species.filter(name__name='Осина'):
            aspen = contract.plot.plot_wood_species.filter(name__name='Осина')
        else:
            aspen = False
        if birch:
            self.page['BP84'] = birch[0].number_of_trees
            self.page['BP85'] = birch[0].large
            self.page['BP86'] = birch[0].average
            self.page['BP87'] = birch[0].small
            self.page['BP88'] = birch[0].firewood
            self.page['BP89'] = birch[0].brushwood

        if aspen:
            self.page['BP94'] = aspen[0].number_of_trees
            self.page['BP95'] = aspen[0].large
            self.page['BP96'] = aspen[0].average
            self.page['BP97'] = aspen[0].small
            self.page['BP98'] = aspen[0].firewood
            self.page['BP99'] = aspen[0].brushwood'''
        form = {'person': contract.statement.person,
                'contract': contract,
                'bank_detail': bank_detail,
                'organ_repr': organ_repr,
                'pk': pk,
                'title': 'Добавить данные по породе в деляне к договору' + str(contract.number)}
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
            if plot_wood_species.price is None:
                plot_wood_species.price = 0
            if plot_wood_species.large is None:
                plot_wood_species.large = 0
            if plot_wood_species.average is None:
                plot_wood_species.average = 0
            if plot_wood_species.small is None:
                plot_wood_species.small = 0
            if plot_wood_species.firewood is None:
                plot_wood_species.firewood = 0
            if plot_wood_species.brushwood is None:
                plot_wood_species.brushwood = 0
            plot_wood_species.save()
            if plot.business is None:
                plot.business = 0
            if plot.firewood is None:
                plot.firewood = 0
            if plot.brushwood is None:
                plot.brushwood = 0
            if plot.liquid_wood is None:
                plot.liquid_wood = 0
            if plot.total is None:
                plot.total = 0
            plot.plot_wood_species.add(plot_wood_species)
            plot.save()
            return redirect('contract_view', pk=contract.pk)
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class PlotWoodSpeciesMod(CreateView):
    template_name = 'sobnushdi/plot_wood_species/plot_wood_species_mod.html'

    def get(self, request, pk=None, *args, **kwargs):
        plot_wood_species = PlotWoodSpecies.objects.get(pk=pk)
        plot = Plot.objects.get(plot_wood_species=plot_wood_species)
        contract = Contract.objects.get(plot=plot)
        person = contract.statement.person
        form_mod_plot_wood_species = AddPlotWoodSpecies(instance=plot_wood_species)
        form = {
            'person': person,
            'contract': contract,
            'plot': plot,
            'pk': pk,
            'form_mod_plot_wood_species': form_mod_plot_wood_species,
            'title': 'contract.number'}
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
            plot.plot_wood_species.add(plot_wood_species)
            plot.save()
            return redirect('contract_view', pk=contract.pk)
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)
