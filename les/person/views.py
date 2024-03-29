from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View

from .forms import *


class LocalityTypeAddOrMod(CreateView):
    template_name = 'locality_types/locality_type_mod.html'
    paginate_by = 10

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            locality_type = LocalityType.objects.get(pk=pk)
            form_mod_locality_type = AddLocalityType(instance=locality_type)
        else:
            form_mod_locality_type = AddLocalityType()
        form = {'form_mod_locality_type': form_mod_locality_type,
                'pk': pk,
                'title': 'Добавить тип населенного пункта'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            locality_type = LocalityType.objects.get(pk=pk)
            form_mod_locality_type = AddLocalityType(request.POST, instance=locality_type)
        else:
            form_mod_locality_type = AddLocalityType(request.POST)
        form = {'form_mod_locality_type': form_mod_locality_type,
                'title': 'Добавить тип населенного пункта'}
        if form_mod_locality_type.is_valid():
            if pk:
                locality_type.save()
            else:
                form_mod_locality_type.save()
            return redirect('locality_types_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class LocalityTypesList(ListView):
    model = LocalityType
    template_name = 'locality_types/locality_types_list.html'
    context_object_name = 'locality_types'
    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        gg = self.model.objects.all()
        print(gg)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Типы населенных пунктов'
        return context


class PersonAdd(CreateView):
    template_name = 'person/person_add.html'

    def get(self, request, *args, **kwargs):
        form_add_person = AddPerson()
        form_add_passport = AddPersonPassport()
        form_add_residence_address = AddPersonResidenceAddress()
        form_add_person_representative = AddRepresentativePerson()
        form_add_passport_representative = AddRepresentativePassport()
        form_add_residence_address_representative = AddRepresentativeResidenceAddress()
        form = {'form_add_person': form_add_person,
                'form_add_passport': form_add_passport,
                'form_add_residence_address': form_add_residence_address,
                'form_add_person_representative': form_add_person_representative,
                'form_add_passport_representative': form_add_passport_representative,
                'form_add_residence_address_representative': form_add_residence_address_representative,
                'title': 'Добавить заявителя'}
        return render(request, self.template_name, context=form)

    def post(self, request, *args, **kwargs):
        form_add_person = AddPerson(request.POST)
        form_add_passport = AddPersonPassport(request.POST)
        form_add_residence_address = AddPersonResidenceAddress(request.POST)
        form_add_person_representative = AddRepresentativePerson(request.POST)
        form_add_passport_representative = AddRepresentativePassport(request.POST)
        form_add_residence_address_representative = AddRepresentativeResidenceAddress(request.POST)
        form = {'form_add_person': form_add_person,
                'form_add_person_passport': form_add_passport,
                'form_add_person_residence_address': form_add_residence_address,
                'form_add_representative': form_add_person_representative,
                'form_add_representative_passport': form_add_passport_representative,
                'form_add_representative_residence_address': form_add_residence_address_representative,
                'title': 'Добавить заявителя'}
        if form_add_person.is_valid() and form_add_passport.is_valid() and form_add_residence_address.is_valid():
            passport = form_add_passport.save()
            adr = form_add_residence_address.save()
            pers = form_add_person.save(commit=False)
            pers.passport = passport
            pers.residence_address = adr
            pers.save()
            if form_add_person.cleaned_data.get('there_is_a_representative'):
                if form_add_person_representative.is_valid() and form_add_passport_representative.is_valid()\
                        and form_add_residence_address_representative.is_valid():
                    adr_representative = form_add_residence_address_representative.save()
                    passp_representative = form_add_passport_representative.save()
                    pers_representative = form_add_person_representative.save(commit=False)
                    pers_representative.residence_address = adr_representative
                    pers_representative.passport = passp_representative
                    pers_representative.person = pers
                    pers_representative.save()
            return redirect('persons_list')
        return render(request, self.template_name, context=form)


class PersonMod(View):
    template_name = 'person/person_mod.html'

    def get(self, request, pk, *args, **kwargs):
        pers = get_object_or_404(Person, pk=pk)
        date_of_bird = str(pers.date_of_bird)
        date_of_issue = str(pers.passport.date_of_issue)
        form_mod_person = AddPerson(initial={'date_of_bird': date_of_bird}, instance=pers)
        form_mod_passport = AddPersonPassport(initial={'date_of_issue': date_of_issue}, instance=pers.passport)
        form_mod_residence_address = AddPersonResidenceAddress(instance=pers.residence_address)
        form_mod_person_representative = AddRepresentativePerson()
        form_mod_passport_representative = AddRepresentativePassport()
        form_mod_residence_address_representative = AddRepresentativeResidenceAddress()
        if pers.there_is_a_representative:
            pers_representative = get_object_or_404(RepresentativePerson, person__pk=pk)
            form_mod_person_representative = AddRepresentativePerson(instance=pers_representative)
            form_mod_passport_representative = AddRepresentativePassport(instance=pers_representative.passport)
            form_mod_residence_address_representative = AddRepresentativeResidenceAddress(
                                                                instance=pers_representative.residence_address)
        form = {'form_mod_person': form_mod_person,
                'form_mod_passport': form_mod_passport,
                'form_mod_residence_address': form_mod_residence_address,
                'form_mod_person_representative': form_mod_person_representative,
                'form_mod_representative_passport': form_mod_passport_representative,
                'form_mod_representative_residence_address': form_mod_residence_address_representative,
                'pk': pk,
                'title': 'Изменить данные заявителя'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        pers = get_object_or_404(Person, pk=pk)
        pers_passport = pers.passport
        pers_address = pers.residence_address
        form_mod_person = AddPerson(request.POST, instance=pers)
        form_mod_passport = AddPersonPassport(request.POST, instance=pers_passport)
        form_mod_residence_address = AddPersonResidenceAddress(request.POST, instance=pers_address)
        form_mod_person_representative = AddRepresentativePerson(request.POST)
        form_mod_passport_representative = AddRepresentativePassport(request.POST)
        form_mod_residence_address_representative = AddRepresentativeResidenceAddress(request.POST)
        if pers.there_is_a_representative:
            pers_representative = get_object_or_404(RepresentativePerson, person__pk=pk)
            pers_representative_passport = pers_representative.passport
            pers_representative_address = pers_representative.residence_address
            form_mod_person_representative = AddRepresentativePerson(request.POST, instance=pers_representative)
            form_mod_passport_representative = AddRepresentativePassport(request.POST,
                                                                         instance=pers_representative_passport)
            form_mod_residence_address_representative = AddRepresentativeResidenceAddress(request.POST,
                                                                                          instance=pers_representative_address)
        form = {'form_mod_person': form_mod_person,
                'form_mod_passport': form_mod_passport,
                'form_mod_residence_address': form_mod_residence_address,
                'form_mod_person_representative': form_mod_person_representative,
                'form_mod_representative_passport': form_mod_passport_representative,
                'form_mod_representative_residence_address': form_mod_residence_address_representative,
                'pk': pk,
                'title': 'Изменить данные заявителя'}
        if form_mod_person.is_valid() and form_mod_passport.is_valid() and form_mod_residence_address.is_valid():
            if form_mod_person_representative.is_valid() and form_mod_passport_representative.is_valid() \
                    and form_mod_residence_address_representative.is_valid():
                print(pers.there_is_a_representative)

                if form_mod_person.cleaned_data.get('there_is_a_representative'):
                    adr_representative = form_mod_residence_address_representative.save()
                    passp_representative = form_mod_passport_representative.save()
                    pers_representative = form_mod_person_representative.save(commit=False)
                    pers_representative.residence_address = adr_representative
                    pers_representative.passport = passp_representative
                    pers_representative.person = pers
                    pers_representative.save()
                elif pers.there_is_a_representative:
                    if pers_representative:
                        pers_representative_passport.save()
                        pers_representative_address.save()
                        pers_representative.save()
                elif not form_mod_person.cleaned_data.get('there_is_a_representative'):
                    pers_representative_passport.delete()
                    pers_representative_address.delete()
                    pers_representative.delete()
            pers_passport.save()
            pers_address.save()
            pers.save()
            return redirect('persons_list')

        return render(request, self.template_name, context=form)


class PersonView(ListView):
    model = Person
    template_name = 'person/persons_list.html'
    context_object_name = 'pers'
    paginate_by = 10
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        for person in self.object_list:
            if person.date_of_bird:
                person.date_of_bird = person.date_of_bird.strftime("%d.%m.%Y")
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявители'
        return context


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'person/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'person/login.html'
    success_url = reverse_lazy('persons_list')


def logout_user(request):
    logout(request)
    return redirect('login')
