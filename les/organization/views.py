from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .forms import *

from .sklonenye import *


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
            # form_add_address_otdelenya = AddAddressOtdelenya(instance=organization.address_otdelenya)
            form_add_requisites_organization = AddRequisitesOrganization(instance=organization.requisites_organization)
        else:
            print(' Запрос  GET - Нет PK')
            form_add_organization = AddOrganization()
            form_add_organization_address = AddOrganizationAddress()
            # form_add_address_otdelenya = AddAddressOtdelenya()
            form_add_requisites_organization = AddRequisitesOrganization()

        form = {'form_add_organization': form_add_organization,
                'form_add_organization_address': form_add_organization_address,
                # 'form_add_address_otdelenya': form_add_address_otdelenya,
                'form_add_requisites_organization': form_add_requisites_organization,
                'pk': pk,
                'title': 'Добавить организацию'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            print(' Запрос  POST - Есть PK' )
            organization = Organization.objects.get(pk=pk)
            organization_address = organization.organization_address
            # address_otdelenya = organization.address_otdelenya
            requisites_organization = organization.requisites_organization
            form_add_organization = AddOrganization(request.POST, instance=organization)
            form_add_organization_address = AddOrganizationAddress(request.POST, instance=organization_address)
            # form_add_address_otdelenya = AddAddressOtdelenya(request.POST, instance=address_otdelenya)
            form_add_requisites_organization = AddRequisitesOrganization(request.POST, instance=requisites_organization)
        else:
            print(' Запрос  POST - Нет PK')
            form_add_organization = AddOrganization(request.POST)
            form_add_organization_address = AddOrganizationAddress(request.POST)
            # form_add_address_otdelenya = AddAddressOtdelenya(request.POST)
            form_add_requisites_organization = AddRequisitesOrganization(request.POST)
        form = {'form_add_organization': form_add_organization,
                'form_add_organization_address': form_add_organization_address,
                # 'form_add_address_otdelenya': form_add_address_otdelenya,
                'form_add_requisites_organization': form_add_requisites_organization,
                'pk': pk,
                'title1': 'Добавить организацию'}
        if form_add_organization.is_valid() and form_add_organization_address.is_valid() and \
                form_add_requisites_organization.is_valid():
            if pk:
                if organization.selected:
                    org = Organization.objects.exclude(pk=pk)  #
                    for i in org:                              # Отключение активной организации
                        i.selected = False                     #
                        i.save()                               #
                print('Запрос POST отправка на сервер Есть PK')
                skl = sklonenye(organization.title, typee='Orgn')
                organization.title_v_predlojnom_padeje = skl[1]
                organization.title_v_roditelnom_padeje = skl[0]
                organization_address.save()
                #address_otdelenya.save()
                requisites_organization.save()
                organization.save()
            else:
                print('Запрос POST отправка на сервер Нет PK создание нового')
                adr = form_add_organization_address.save()
                # adr_otd = form_add_address_otdelenya.save()
                requisites = form_add_requisites_organization.save()
                organization = form_add_organization.save(commit=False)
                skl = sklonenye(organization.title, typee='Orgn')
                organization.title_v_predlojnom_padeje = skl[1]
                organization.title_v_roditelnom_padeje = skl[0]
                if organization.selected:
                    org = Organization.objects.exclude(pk=pk)  #
                    for i in org:                              # Отключение активной организации
                        i.selected = False                     #
                        i.save()                               #
                organization.organization_address = adr
                # organization.address_otdelenya = adr_otd
                organization.requisites_organization = requisites
                organization.save()
            return redirect('organizations_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class RepresentativeList(ListView):
    model = DepartmentRepresentative
    template_name = 'representatives/representatives_list.html'
    context_object_name = 'representative'
    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['org_pk'])
        context['org_pk'] = self.kwargs['org_pk']
        return context

    def get_queryset(self):
        return DepartmentRepresentative.objects.filter(organization=self.kwargs['org_pk'])


class RepresentativeAddOrMod(CreateView):
    template_name = 'representatives/representative_mod.html'
    context_object_name = 'representative'

    def get(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        if pk:
            print(' Запрос  GET - Есть PK')
            representative = DepartmentRepresentative.objects.get(pk=pk)
            form_mod_representative_organization = AddOrModRepresentativeOrganization(instance=representative)
        else:
            print(' Запрос  GET - Нет PK')
            form_mod_representative_organization = AddOrModRepresentativeOrganization()
        form = {'form_mod_representative_organization': form_mod_representative_organization,
                'org': organization.pk,
                'pk': pk,
                'title': 'Представитель организации'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        if pk:
            print(' Запрос  POST - Есть PK')
            representative = DepartmentRepresentative.objects.get(pk=pk)
            form_mod_representative_organization = AddOrModRepresentativeOrganization(
                request.POST, instance=representative)
        else:
            print(' Запрос  POST - Нет PK')
            form_mod_representative_organization = AddOrModRepresentativeOrganization(request.POST)
        form = {'form_mod_representative_organization': form_mod_representative_organization,
                'pk': pk,
                'org': organization.pk,
                'title1': 'Представитель организации'}
        if form_mod_representative_organization.is_valid():
            if pk:
                rep = DepartmentRepresentative.objects.exclude(pk=pk)  #
                for i in rep:  # Отключение активной организации
                    i.selected = False  #
                    i.save()  #
                print('Запрос POST отправка на сервер Есть PK')
                skl_second_name = sklonenye(representative.second_name, typee='Surn')[0]
                skl_firs_name = sklonenye(representative.first_name, typee='Name')[0]
                skl_patronymic_name = sklonenye(representative.patronymic, typee='Patr')[0]
                representative.fio_v_roditelnom_padeje = skl_second_name + ' ' + skl_firs_name + ' ' \
                                                         + skl_patronymic_name
                representative.position_v_roditelnom_padeje = sklonenye(representative.position)[0]
                representative.save()
            else:
                print('Запрос POST отправка на сервер Нет PK')
                representative = form_mod_representative_organization.save(commit=False)
                rep = DepartmentRepresentative.objects.exclude(pk=pk)  #
                if representative.selected:#
                    for i in rep:  # Отключение активной организации
                        i.selected = False  #
                        i.save()  #
                representative.organization = Organization.objects.get(pk=self.kwargs['org_pk'])
                skl_second_name = sklonenye(representative.second_name)[0]
                skl_firs_name = sklonenye(representative.first_name)[0]
                skl_patronymic_name = sklonenye(representative.patronymic)[0]
                representative.fio_v_roditelnom_padeje = skl_second_name + ' ' + skl_firs_name + ' ' + skl_patronymic_name
                representative.position_v_roditelnom_padeje = sklonenye(representative.position)[0]
                representative.save()
            return redirect('representative_list', organization.pk)

        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class BankDetailsList(ListView):
    model = BankDetails
    template_name = 'bank_details/bank_details_list.html'
    context_object_name = 'bank_details'
    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['org_pk'])
        context['org_pk'] = self.kwargs['org_pk']
        return context

    def get_queryset(self):
        return BankDetails.objects.filter(organization=self.kwargs['org_pk'])


class BankDetailsAddOrMod(CreateView):
    template_name = 'bank_details/bank_details_mod.html'
    context_object_name = 'bank_details'

    def get(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        if pk:
            print(' Запрос  GET - Есть PK')
            bank_details = BankDetails.objects.get(pk=pk)
            form_mod_bank_details = AddOrModBankDetals(instance=bank_details)
        else:
            print(' Запрос  GET - Нет PK')
            form_mod_bank_details = AddOrModBankDetals()
        form = {'form_mod_bank_details': form_mod_bank_details,
                'org': organization.pk,
                'pk': pk,
                'title': 'Банковские реквизиты'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        if pk:
            print(' Запрос  POST - Есть PK')
            bank_details = BankDetails.objects.get(pk=pk)
            form_mod_bank_details = AddOrModBankDetals(
                request.POST, instance=bank_details)
        else:
            print(' Запрос  POST - Нет PK')
            form_mod_bank_details = AddOrModBankDetals(request.POST)
        form = {'form_mod_bank_details': form_mod_bank_details,
                'pk': pk,
                'org': organization.pk,
                'title': 'Банковские реквизиты'}
        if form_mod_bank_details.is_valid():
            if pk:
                print('Запрос POST отправка на сервер Есть PK')
                bank_det = BankDetails.objects.exclude(pk=pk)  #
                if bank_details.selected:  #
                    for i in bank_det:  # Отключение активной организации
                        i.selected = False  #
                        i.save()  #
                bank_details.save()
            else:
                print('Запрос POST отправка на сервер Нет PK')
                bank_details = form_mod_bank_details.save(commit=False)
                bank_det = BankDetails.objects.exclude(pk=pk)  #
                if bank_details.selected:  #
                    for i in bank_det:  # Отключение активной организации
                        i.selected = False  #
                        i.save()  #
                bank_details.organization = Organization.objects.get(pk=self.kwargs['org_pk'])
                bank_details.save()
            return redirect('bank_details_list', organization.pk)

        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class DepartmentList(ListView):
    model = Department
    template_name = 'departments/departments_list.html'
    context_object_name = 'department'
    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print('список отделов org_pk=', self.kwargs['org_pk'])
        context['org_pk'] = self.kwargs['org_pk']
        return context


class DepartmentAddOrMod(CreateView):
    template_name = 'departments/department_mod.html'
    context_object_name = 'departments'

    def get(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        if pk:
            department = Department.objects.get(pk=pk)
            form_mod_department = AddOrModDepartment(instance=department)
        else:
            print(' Запрос  GET - Нет PK')
            form_mod_department = AddOrModDepartment()
        form = {'form_mod_department': form_mod_department,
                'org': organization.pk,
                'pk': pk,
                'title': 'Отдел (лесничество)'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        if pk:
            department = Department.objects.get(pk=pk)
            form_mod_department = AddOrModDepartment(
                request.POST, instance=department)
        else:
            form_mod_department = AddOrModDepartment(request.POST)
        form = {'form_mod_departments': form_mod_department,
                'pk': pk,
                'org': organization.pk,
                'title': 'Банковские реквизиты'}
        if form_mod_department.is_valid():
            if pk:
                department.save()
            else:
                print('Запрос POST отправка на сервер Нет PK')
                department = form_mod_department.save(commit=False)
                department.organization = Organization.objects.get(pk=self.kwargs['org_pk'])
                department.save()
            return redirect('departments_list', organization.pk)

        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class DepartmentAddressList(ListView):
    model = DepartmentAddress
    template_name = 'departments/department_address_list.html'
    context_object_name = 'department_address'
    ordering = '-pk'
    paginate_by = 10

    def get_queryset(self):
        return DepartmentAddress.objects.filter(department=Department.objects.get(pk=self.kwargs['dep_pk']))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print('org_pk=', self.kwargs['org_pk'])
        print('dep_pk=', self.kwargs['dep_pk'])
        context['org_pk'] = self.kwargs['org_pk']
        context['dep_pk'] = self.kwargs['dep_pk']
        return context


class DepartmentAddressAddOrMod(CreateView):
    template_name = 'departments/department_address_mod.html'
    context_object_name = 'department_address'

    def get(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        department = Department.objects.get(pk=self.kwargs['dep_pk'])
        if pk:
            department_address = DepartmentAddress.objects.get(pk=pk)
            form_mod_department_address = AddOrModDepartmentAddress(
                instance=department_address)
        else:
            form_mod_department_address = AddOrModDepartmentAddress()
        form = {'form_mod_department_address': form_mod_department_address,
                'org': organization.pk,
                'dep': department.pk,
                'pk': pk,
                'title': 'Адрес отдела (лесничества)'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk=None, *args, **kwargs):
        organization = Organization.objects.get(pk=self.kwargs['org_pk'])
        department = Department.objects.get(pk=self.kwargs['dep_pk'])
        if pk:
            department_address = DepartmentAddress.objects.get(pk=pk)
            form_mod_department_address = AddOrModDepartmentAddress(
                request.POST, instance=department_address)
        else:
            form_mod_department_address = AddOrModDepartmentAddress(request.POST)
        form = {'form_mod_department_address': form_mod_department_address,
                'pk': pk,
                'org': organization.pk,
                'dep': department.pk,
                'title': 'Банковские реквизиты'}
        if form_mod_department_address.is_valid():
            if pk:
                department_address.save()
            else:
                department_address = form_mod_department_address.save(commit=False)
                department_address.department = Department.objects.get(pk=self.kwargs['dep_pk'])
                department_address.save()
            return redirect('department_address_list', organization.pk, department.pk)

        else:
            form_p = form
        return render(request, self.template_name, context=form_p)
