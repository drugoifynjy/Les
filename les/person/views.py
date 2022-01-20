from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView


from .forms import *


def person_add(request):
    if request.method == 'POST':
        form1 = AddPerson(request.POST)
        form2 = AddPassport(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save(commit=False)
            form2.person = form1
            form2.save()
            return redirect('person_list')
    else:
        form1 = AddPerson()
        form2 = AddPassport()
        cont = {'form1': form1,
                'form2': form2,
                'title': 'Добавить заявителя'}
        return render(request, 'person/person_add.html', context=cont)



def person_mod(request, pk):
    print(pk)
    post = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = AddPerson(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = AddPerson(instance=post)
    return render(request, 'person/person_mod.html', {'form': form, 'pk': pk, 'title': 'редактироние заявителя'})


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
