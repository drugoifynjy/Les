from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View
from formtools.wizard.views import SessionWizardView
from .forms import *


class PersonAdd(CreateView):
    template_name = 'person/person_add.html'

    def get(self, request, *args, **kwargs):
        form_add_person = AddPerson()
        form_add_passport = AddPassport()
        form_add_residence_address = AddResidenceAddress()
        form = {'form_add_person': form_add_person,
                'form_add_passport': form_add_passport,
                'form_add_residence_address': form_add_residence_address,
                'title': 'Добавить заявителя'}
        return render(request, self.template_name, context=form)

    def post(self, request, *args, **kwargs):
        form_add_person = AddPerson(request.POST)
        form_add_passport = AddPassport(request.POST)
        form_add_residence_address = AddResidenceAddress(request.POST)
        form = {'form_add_person': form_add_person,
                'form_add_passport': form_add_passport,
                'form_add_residence_address': form_add_residence_address,
                'title': 'Добавить заявителя'}
        if form_add_person.is_valid() and form_add_passport.is_valid() and form_add_residence_address.is_valid():
            adr = form_add_residence_address.save()
            passport = form_add_passport.save()
            pers = form_add_person.save(commit=False)
            pers.passport = passport
            pers.residence_address = adr
            pers.save()
            return redirect(request.META['HTTP_REFERER'])

        return render(request, self.template_name, context=form)


class PersonMod(View):
    template_name = 'person/person_mod.html'
    model = Person

    def get(self, request, pk, *args, **kwargs):
        pers = get_object_or_404(Person, pk=pk)
        date_of_bird = str(pers.date_of_bird)
        date_of_issue = str(pers.passport.date_of_issue)
        form_person_mod = AddPerson(initial={'date_of_bird': date_of_bird}, instance=pers)
        form_passport_mod = AddPassport(initial={'date_of_issue': date_of_issue}, instance=pers.passport)
        form_residence_address_mod = AddResidenceAddress(instance=pers.residence_address)
        form = {'form_person_mod': form_person_mod,
                'form_passport_mod': form_passport_mod,
                'form_residence_address_mod': form_residence_address_mod,
                'pk': pk,
                'title': 'Добавить заявителя'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        person = get_object_or_404(Person, pk=pk)
        passport = person.passport
        address = person.residence_address
        form_mod_person = AddPerson(request.POST, instance=person)
        form_passport_mod = AddPassport(request.POST, instance=passport)
        form_residence_address_mod = AddResidenceAddress(request.POST, instance=address)

        form = {'form_mod_person': form_mod_person,
                'form_passport_mod': form_passport_mod,
                'form_residence_address_mod': form_residence_address_mod,
                'pk': pk,
                'title': 'Добавить заявителя'}
        if form_mod_person.is_valid() and form_passport_mod.is_valid() and form_residence_address_mod.is_valid():
            passport.save()
            address.save()
            person.save()
            return redirect('persons_list')

        return render(request, self.template_name, context=form)

# def person_mod(request, pk):
#     pers = get_object_or_404(Person, pk=pk)
#     addr = pers.residence_address
#     passp = pers.passport
#     if request.method == 'POST':
#         form_person_mod = AddPerson(request.POST, instance=pers)
#         form_passport_mod = AddPassport(request.POST, instance=passp)
#         form_residence_address_mod = AddResidenceAddress(request.POST, instance=addr)
#         if form_person_mod.is_valid() and form_passport_mod.is_valid() and form_residence_address_mod.is_valid():
#             form_person_mod.save()
#             form_passport_mod.save()
#             form_residence_address_mod.save()
#             return redirect('person_list')
#     else:
#         form_person_mod = AddPerson(instance=pers)
#         form_passport_mod = AddPassport(instance=passp)
#         form_residence_address_mod = AddResidenceAddress(instance=addr)
#
#         cont = {'form_person_mod': form_person_mod,
#                 'form_passport_mod': form_passport_mod,
#                 'form_residence_address_mod': form_residence_address_mod,
#                 'pk': pk,
#                 'title': 'Изменить заявителя'}
#         return render(request, 'person/person_mod.html', context=cont)


class PersonView(ListView):
    model = Person
    template_name = 'person/persons_list.html'
    context_object_name = 'pers'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявители'
        return context


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'person/register.html'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'person/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')
