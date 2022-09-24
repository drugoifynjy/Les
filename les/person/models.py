from django.db import models
from .models_abstact import *


class PersonResidenceAddress(Address):

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес проживания заявителя'
        verbose_name_plural = 'Адреса проживания заявителей'


class RepresentativeResidenceAddress(Address):

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес проживания представителя заявителя'
        verbose_name_plural = 'Адреса проживания представителей заявителей'


class PersonPassport(Passport):
    class Meta:
        ordering = ['id']
        verbose_name = 'Паспортные данные заявителя'
        verbose_name_plural = 'Паспортные данные заявителей'


class RepresentativePassport(Passport):
    class Meta:
        ordering = ['id']
        verbose_name = 'Паспортные данные представителя заявителя'
        verbose_name_plural = 'Паспортные данные представителей заявителей'


class Person(models.Model):
    second_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    date_of_bird = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='Телефон')
    residence_address = models.OneToOneField(PersonResidenceAddress, on_delete=models.CASCADE,
                                             blank=True, null=True, verbose_name='Адрес проживания')
    passport = models.OneToOneField(PersonPassport, on_delete=models.CASCADE,
                                    blank=True, null=True, verbose_name='паспортные данные')
    there_is_a_representative = models.BooleanField(verbose_name='есть представитель', default=False)

    def __str__(self):
        a = str(self.second_name)+' '+str(self.first_name)+' '+str(self.patronymic) + " - заявитель"
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'ФИО заявителя'
        verbose_name_plural = 'ФИО заявтиелей'


class RepresentativePerson(models.Model):
    """Представитель заявителя по доверенности"""
    second_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    date_of_bird = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='Телефон')
    residence_address = models.OneToOneField(RepresentativeResidenceAddress, on_delete=models.CASCADE,
                                               blank=True, null=True, verbose_name='Адрес регистрации')
    passport = models.OneToOneField(RepresentativePassport, on_delete=models.CASCADE,
                                      blank=True, null=True, verbose_name='паспортные данные')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='Заявитель')

    def __str__(self):
        a = str(self.second_name)+' '+str(self.first_name)+' '+str(self.patronymic) + " - представитель заявителя" +\
            self.person.__str__()

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'ФИО представителя покупателя'
        verbose_name_plural = 'ФИО представителей покупателей'
