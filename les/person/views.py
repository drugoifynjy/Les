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
    print(pk)
    post = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form1 = AddPerson(request.POST, instance=post)
        if form1.is_valid():
            form1.save()
            return redirect('person_list')
    else:
        form1 = AddPerson(instance=post)
    return render(request, 'person/person_mod.html', {'form': form1, 'pk': pk, 'title': 'редактироние заявителя'})


def passport_mod(request, pk):
    print(pk)
    if hasattr(Person(pk), 'passport'):
        print(Passport(pk=pk))
        post = get_object_or_404(Passport, pk=pk)
        if request.method == 'POST':
            form = AddPassport(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('person_list')
        else:
            form = AddPassport(instance=post)
        return render(request, 'person/passport_mod.html',
                      {'form': form, 'pk': pk, 'title': 'редактироние паспортных данных'})
    else:
        if request.method == 'POST':
            form = AddPassport(request.POST)
            if form.is_valid():
                form.save()
                return redirect('passport_list')
        else:
            form = AddPassport()
        return render(request, 'person/passport_add.html',
                      {'form': form, 'title': 'Добавить паспортные данные'})


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
