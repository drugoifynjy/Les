from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView


from .forms import *


def person_add(request):
    if request.method == 'POST':
        form_add_person = AddPerson(request.POST)
        form_add_passport = AddPassport(request.POST)
        form_add_residence_address = AddResidenceAddress(request.POST)
        if form_add_residence_address.is_valid() and form_add_passport.is_valid() and form_add_person.is_valid():
            adr = form_add_residence_address.save()
            passport = form_add_passport.save()
            pers = form_add_person.save(commit=False)
            pers.passport = passport
            pers.residence_address = adr
            pers.save()
            return redirect('person_list')
    else:
        form_add_person = AddPerson()
        form_add_passport = AddPassport()
        form_add_residence_address = AddResidenceAddress()
        cont = {'form_add_person': form_add_person,
                'form_add_passport': form_add_passport,
                'form_add_residence_address': form_add_residence_address,
                'title': 'Добавить заявителя'}
        return render(request, 'person/person_add.html', context=cont)


def person_mod(request, pk):
    pers = get_object_or_404(Person, pk=pk)
    addr = pers.residence_address
    passp = pers.passport
    if request.method == 'POST':
        form_person_mod = AddPerson(request.POST, instance=pers)
        form_passport_mod = AddPassport(request.POST, instance=passp)
        form_residence_address_mod = AddResidenceAddress(request.POST, instance=addr)
        if form_person_mod.is_valid() and form_passport_mod.is_valid() and form_residence_address_mod.is_valid():
            form_person_mod.save()
            form_passport_mod.save()
            form_residence_address_mod.save()
            return redirect('person_list')
    else:
        form_person_mod = AddPerson(instance=pers)
        form_passport_mod = AddPassport(instance=passp)
        form_residence_address_mod = AddResidenceAddress(instance=addr)

        cont = {'form_person_mod': form_person_mod,
                'form_passport_mod': form_passport_mod,
                'form_residence_address_mod': form_residence_address_mod,
                'pk': pk,
                'title': 'Добавить заявителя'}
        return render(request, 'person/person_mod.html', context=cont)


class PersonView(ListView):
    model = Person
    template_name = 'person/person_list.html'


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'person/register.html'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'person/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')
