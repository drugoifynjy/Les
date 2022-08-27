from openpyxl import load_workbook
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View, DeleteView
from datetime import timedelta
from .forms import *

from sobnushdi.models import Statement


class OrganizationsView(ListView):
    model = Organization
    template_name = 'organizations/organizations_list.html'
    context_object_name = 'organizations'
    ordering = '-pk'
    paginate_by = 10


class OrganizationAddOrMod(CreateView):
    template_name = 'organizations/organization_mod.html'

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            print(' Запрос  GET - Есть PK')
            organization = Organization.objects.get(pk=pk)
            form_add_organization = AddOrganization(instance=organization)
            form_add_organization_address = AddOrganizationAddress(instance=organization.organization_address)
            form_add_requisites_organization = AddRequisitesOrganization(instance=organization.requisites_organization)
            form_add_bank_details = AddBankDetals(instance=BankDetails)
        else:
            print(' Запрос  GET - Нет PK')
            form_add_organization = AddOrganization()
            form_add_organization_address = AddOrganizationAddress()
            form_add_requisites_organization = AddRequisitesOrganization()

        form = {'form_add_organization': form_add_organization,
                'form_add_organization_address': form_add_organization_address,
                'form_add_requisites_organization': form_add_requisites_organization,
                'pk': pk,
                'title': 'Добавить организацию'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            print(' Запрос  POST - Есть PK' )
            organization = Organization.objects.get(pk=pk)
            organization_address = organization.organization_address
            requisites_organization = organization.requisites_organization
            form_add_organization = AddOrganization(request.POST, instance=organization)
            form_add_organization_address = AddOrganizationAddress(request.POST, instance=organization_address)
            form_add_requisites_organization = AddRequisitesOrganization(request.POST, instance=requisites_organization)
        else:
            print(' Запрос  POST - Нет PK')
            form_add_organization = AddOrganization(request.POST)
            form_add_organization_address = AddOrganizationAddress(request.POST)
            form_add_requisites_organization = AddRequisitesOrganization(request.POST)
        form = {'form_add_organization': form_add_organization,
                'form_add_organization_address': form_add_organization_address,
                'form_add_requisites_organization': form_add_requisites_organization,
                'pk': pk,
                'title1': 'Добавить организацию'}
        if form_add_organization.is_valid() and form_add_organization_address.is_valid() and form_add_requisites_organization.is_valid():
            if pk:
                print('Запрос POST отправка на сервер Есть PK')
                organization_address.save()
                requisites_organization.save()
                organization.save()
            else:
                print('Запрос POST отправка на сервер Нет PK создание нового')
                adr = form_add_organization_address.save()
                requisites = form_add_requisites_organization.save()
                organization = form_add_organization.save(commit=False)
                organization.organization_address = adr
                organization.requisites_organization = requisites
                organization.save()
            return redirect('organizations_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class RepresentativeList(ListView):
    model = OrganizationRepresentative
    template_name = 'representatives/representative_list.html'
    context_object_name = 'representative'
    ordering = '-pk'
    paginate_by = 10

    def get_queryset(self):
        return OrganizationRepresentative.objects.filter(organization=self.kwargs['org_pk'])


class RepresentativeAddOrMod(CreateView):
    template_name = 'representatives/representative_mod.html'

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            print(' Запрос  GET - Есть PK')
            representative = OrganizationRepresentative.objects.get(pk=pk)
            form_mod_representative_organization = AddOrModRepresentativeOrganization(instance=representative)
        else:
            print(' Запрос  GET - Нет PK')
            form_mod_representative_organization = AddOrModRepresentativeOrganization()
        form = {'form_mod_representative_organization': form_mod_representative_organization,
                'pk': pk,
                'title': 'Добавить представителя организации'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            print(' Запрос  POST - Есть PK')
            representative = OrganizationRepresentative.objects.get(pk=pk)
            form_mod_representative_organization = AddOrModRepresentativeOrganization(
                request.POST, instance=representative)
        else:
            print(' Запрос  POST - Нет PK')
            form_mod_representative_organization = AddOrModRepresentativeOrganization(request.POST)
        form = {'form_mod_representative_organization': form_mod_representative_organization,
                'pk': pk,
                'title1': 'Добавить представителя организации'}
        if form_mod_representative_organization.is_valid():
            if pk:
                print('Запрос POST отправка на сервер Есть PK')
                representative.save()
            else:
                print('Запрос POST отправка на сервер Нет PK')
                representative = form_mod_representative_organization.save(commit=False)
                representative.save()
            return redirect('representative_list')

        else:
            form_p = form
        return render(request, self.template_name, context=form_p)
