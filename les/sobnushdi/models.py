from django.db import models

from person.models import Person


class HeatedPremise(models.Model):
    cadastral_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Кадастровый номер')
    postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name='Индекс')
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name='Район')
    locality = models.CharField(max_length=50, blank=True, null=True, verbose_name='Населенный пункт')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(max_length=6, blank=True, null=True, verbose_name='Дом')
    apartment_number = models.PositiveSmallIntegerField(max_length=6, blank=True, null=True, verbose_name='Квартира')

    def __str__(self):
        if self.apartment_number:
            a = str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__()) + ' кв. ' + \
                str(self.apartment_number.__str__())
        else:
            a = str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__())
        return a

    class Meta:
        verbose_name = 'Адрес отапливаемого помещения'
        verbose_name_plural = 'Адреса отапливаемых помещений'


class Statement(models.Model):
    number_statement = models.PositiveSmallIntegerField(verbose_name='Номер заявления')
    date = models.DateField(blank=True, null=True, verbose_name='Дата заявления')
    address = models.ForeignKey(HeatedPremise, on_delete=models.SET_NULL,
                                null=True, verbose_name='Адрес отапливаемого помещения')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заявитель')

    def __str__(self):
        num = str(self.number_statement)
        data = str(self.date)
        a = str('№  ' + num + ' от ' + data)
        return a

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class Contract(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE, verbose_name='Заявление')
    number_decree = models.CharField(max_length=7, verbose_name='номер распоряжения')
    date_decree = models.DateField(blank=True, null=True, verbose_name='дата распоряжения')
    number = models.CharField(max_length=7, blank=True, null=True, verbose_name='номер договора')
    date = models.DateField(blank=True, null=True, verbose_name='Дата договора')

    def __str__(self):
        b = str(self.statement.person)
        a = ' Заявитель ' + b
        return a

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Plot(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Договор')
    number_plot = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер делянки')
    date = models.DateField(blank=True, null=True, verbose_name='Дата?')
    forestry = models.CharField(max_length=50, blank=True, null=True, verbose_name='Лесничество')
    district_forestry = models.CharField(max_length=50, blank=True, null=True, verbose_name='Участковое лесничество')
    tract = models.CharField(max_length=50, blank=True, null=True, verbose_name='Урочище')
    quarter = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартал')
    section = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Выдел')
    chop_type = models.CharField(max_length=2, verbose_name='Вид рубки')

    def __str__(self):
        a = 'Для договра ' + self.contract.__str__()
        return a

    class Meta:
        verbose_name = 'Делянка'
        verbose_name_plural = 'Делянки'
