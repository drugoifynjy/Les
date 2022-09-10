from django.db import models

from person.models import LocalityType


class DepartmentAddress(models.Model):
    """Адрес отдела(лесничества)"""
    postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name='Индекс', default='644001')
    region = models.CharField(max_length=100, blank=True, null=True, verbose_name='Область', default='Омская')
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name='Район', default='')
    locality_type = models.ForeignKey(LocalityType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип населенноо пункта')
    locality = models.CharField(max_length=50, blank=True, null=True, verbose_name='Населенный пункт',
                                default='')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name='Улица', default='')
    house_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Дом', default='')
    apartment_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартира', default='')

    def __str__(self):
        if self.apartment_number:
            a = str(self.postcode.__str__()) + ' ' + \
                str(self.region.__str__()) + ' область ' + \
                str(self.locality_type) + \
                str(self.locality.__str__()) + \
                str(self.street.__str__()) + ' ул. ' + \
                str(self.house_number.__str__()) + ' кв. ' + \
                str(self.apartment_number.__str__())
        else:
            a = str(self.postcode.__str__()) + ' ' + \
                str(self.region.__str__()) + ' область ' + \
                str(self.locality_type) + \
                str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес отделения(лесничества)'
        verbose_name_plural = 'Адреса отделений(лесничеств)'


class OrganizationAddress(models.Model):
    """Адрес организации"""
    postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name='Индекс', default='644001')
    region = models.CharField(max_length=100, blank=True, null=True, verbose_name='Область', default='Омская')
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name='Район', default='')
    locality_type = models.ForeignKey(LocalityType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип населенноо пункта')
    locality = models.CharField(max_length=50, blank=True, null=True, verbose_name='Населенный пункт',
                                default='Омск')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name='Улица', default='ул. Куйбышева')
    house_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Дом', default='63')
    apartment_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартира', default='')

    def __str__(self):
        if self.apartment_number:
            a = str(self.postcode.__str__()) + ' ' + \
                str(self.region.__str__()) + ' область ' + \
                str(self.locality_type) + \
                str(self.locality.__str__()) + \
                str(self.street.__str__()) + ' ул. ' + \
                str(self.house_number.__str__()) + ' кв. ' + \
                str(self.apartment_number.__str__())
        else:
            a = str(self.postcode.__str__()) + ' ' + \
                str(self.region.__str__()) + ' область ' + \
                str(self.locality_type) + \
                str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес организации'
        verbose_name_plural = 'Адреса организации'


class RequisitesOrganization(models.Model):
    """Реквизиты организации"""
    INN = models.CharField(max_length=10, blank=True, null=True, verbose_name='ИНН', default='')
    KPP = models.CharField(max_length=9, blank=True, null=True, verbose_name='КПП', default='')
    OGRN = models.CharField(max_length=13, blank=True, null=True, verbose_name='ОГРН', default='')
    OKPO = models.CharField(max_length=8, blank=True, null=True, verbose_name='ОКПО', default='')
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name='адрес электронной почты', default='')

    def __str__(self):
        a = 'ИНН ' + str(self.INN) + ' ОГРН ' + str(self.OGRN)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Реквизиты организации'
        verbose_name_plural = 'Реквизиты организаций'


class Organization(models.Model):
    """ Организация """
    title = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Название организации',
                             default='Главное управление лесного хозяйства Омской области')
    title_v_roditelnom_padeje = models.CharField(max_length=1000, blank=True, null=True,
                                                 verbose_name='Название организации в родительном падеже',
                                                 default='')
    title_v_predlojnom_padeje = models.CharField(max_length=1000, blank=True, null=True,
                                                 verbose_name='Название организации в предложном падеже',
                                                 default='')
    organization_address = models.OneToOneField(OrganizationAddress, on_delete=models.CASCADE,
                                             blank=True, null=True, verbose_name='Адрес организации')
    requisites_organization = models.OneToOneField(RequisitesOrganization, on_delete=models.CASCADE,
                                             blank=True, null=True, verbose_name='Реквизиты организации')
    selected = models.BooleanField(verbose_name='Активировать', default=False)

    def __str__(self):
        a = str(self.title)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class BankDetails(models.Model):
    """Банковские реквизиты организации"""
    bank_title = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Название банка',
                            default='ОТДЕЛЕНИЕ ОМСКБАНКА РОССИИ // УФК по Омской области г.Омск')
    bank_account = models.CharField(max_length=20, blank=True, null=True, verbose_name='Расчетный счет', default='')
    correspondent_account = models.CharField(max_length=20, blank=True, null=True, verbose_name='Корсчет', default='')
    BIK = models.CharField(max_length=9, blank=True, null=True, verbose_name='БИК', default='')
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Организация')
    selected = models.BooleanField(verbose_name='Активировать', default=False)

    def __str__(self):
        a = str(self.bank_title)+' '+str(self.bank_account)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Банковские реквизиты организации'
        verbose_name_plural = 'Банковские реквизиты организаций'


class Department(models.Model):
    """Отдел(лесничество)"""
    departments = models.CharField(max_length=500, blank=True, null=True, verbose_name='Название отдела (лесничества)')
    number_department = models.PositiveSmallIntegerField(blank=True, null=True,
                                                         verbose_name='номер отдела (лесничества)')
    address_otdelenya = models.ForeignKey(DepartmentAddress, on_delete=models.SET_NULL, blank=True, null=True,
                                          verbose_name='Адресс отделения(лесничества)')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name='Организация')


class DepartmentRepresentative(models.Model):
    '''Представитель отдела(лесничества)'''
    second_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    fio_v_roditelnom_padeje = models.CharField(max_length=150, blank=True, null=True,
                                               verbose_name='ФИО в родительном падеже')

    position = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Должность')
    position_v_roditelnom_padeje = models.CharField(max_length=1000, blank=True, null=True,
                                                    verbose_name='Должность в родительном пажеде')

    department = models.ForeignKey(Department, blank=True,
                                     null=True, on_delete=models.CASCADE, verbose_name='Отдел')
    #selected = models.BooleanField(verbose_name='Активировать', default=False)

    def __str__(self):
        a = str(self.position)+' '+str(self.second_name)+' '+str(self.first_name)+' '+str(self.patronymic)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Представитель организации'
        verbose_name_plural = 'Представители организаций'


class PowerOfAttorneyRepresentative(models.Model):
    """ Доверенность представителя от организации """
    number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер доверенности')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала действия доверенности')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания действия доверенности')
    organization_representative = models.ForeignKey(DepartmentRepresentative, blank=True,
                                                        null=True, on_delete=models.CASCADE,
                                                        verbose_name='Представитель оотдела(лесничества)')
    #year = models.DateField()
    selected = models.BooleanField(verbose_name='Активировать', default=False)
