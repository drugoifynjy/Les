from django.db import models


class LocalityType(models.Model):
    """Тип населенного пункта: locality_type = ['деревня', 'село', 'город', 'посёлок']"""
    locality_type = models.CharField(max_length=20, blank=True, null=True, verbose_name='Тип населенноо пункта', default='село')
    locality_type_sokr = models.CharField(max_length=5, blank=True, null=True,
                                          verbose_name='Тип населенноо пункта кратко', default='с.')

    def __str__(self):
        a = str(self.locality_type)

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Тип населенного пункта'
        verbose_name_plural = 'Типы населенных пунктов'


class Address(models.Model):
    postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name='Индекс')
    region = models.CharField(max_length=100, blank=True, null=True, default='Омская', verbose_name='Область')
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name='Район')
    locality_type = models.ForeignKey(LocalityType, on_delete=models.SET_NULL,
                                      blank=True, null=True, verbose_name='Тип населенного пункта')
    locality = models.CharField(max_length=50, blank=True, null=True, verbose_name='Населенный пункт')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Дом')
    apartment_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартира')

    def __str__(self):
        if self.apartment_number:
            a = str(self.postcode.__str__()) + ' ' + \
                str(self.region.__str__()) + ' область ' + \
                str(self.district.__str__()) + ' район ' + \
                str(self.locality_type.locality_type_sokr) + \
                str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__()) + ' кв. ' + \
                str(self.apartment_number.__str__())
        else:
            a = str(self.postcode.__str__()) + ' ' + \
                str(self.region.__str__()) + ' область ' + \
                str(self.district.__str__()) + ' район ' + \
                str(self.locality_type) + \
                str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__())
        return a

    class Meta:
        abstract = True


class Passport(models.Model):
    series = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Серия')
    number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер')
    date_of_issue = models.DateField(blank=True, null=True, verbose_name='Дата выдачи')
    issued = models.CharField(max_length=250, blank=True, null=True, verbose_name='Кем выдан')
    address_birth = models.TextField(max_length=500, blank=True, null=True, verbose_name='Место рождения')
    inn = models.PositiveIntegerField(blank=True, null=True, verbose_name='ИНН')

    def __str__(self):
        a = str(self.series.__str__()) + ' ' \
            + str(self.number.__str__()) + ' '\
            + str(self.date_of_issue.__str__()) + ' '\
            + str(self.issued.__str__()) + ' '\
            + str(self.address_birth.__str__()) + ' '
        return a

    class Meta:
        abstract = True


class PersonAbstr(models.Model):
    second_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    date_of_bird = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='Телефон')


    class Meta:
        abstract = True