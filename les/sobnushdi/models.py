from django.db import models

from person.models import Person


class Breeds(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название породы')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


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
        ordering = ['id']
        verbose_name = 'Адрес отапливаемого помещения'
        verbose_name_plural = 'Адреса отапливаемых помещений'


class Statement(models.Model):
    number_statement = models.PositiveSmallIntegerField(verbose_name='Номер заявления')
    date = models.DateField(blank=True, null=True, verbose_name='Дата заявления')
    address = models.ForeignKey(HeatedPremise, on_delete=models.SET_NULL,
                                null=True, verbose_name='Адрес отапливаемого помещения')
    there_is_a_contract = models.BooleanField(verbose_name='Есть договор', default=False)
    refusal_to_conclude_a_contract = models.BooleanField(verbose_name='Отказ от заключения договора', default=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заявитель')

    def __str__(self):
        num = str(self.number_statement)
        data = str(self.date)
        fio = str(self.person)
        a = str('№  ' + num + ' от ' + data + ' ' + fio)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class Contract(models.Model):
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE, verbose_name='Заявление')
    decision_on_statement = models.BooleanField(blank=True, null=True, verbose_name='Отказ')
    number_decree = models.CharField(max_length=7, verbose_name='номер распоряжения')
    date_decree = models.DateField(blank=True, null=True, verbose_name='дата распоряжения')
    number = models.CharField(max_length=7, blank=True, null=True, verbose_name='номер договора')
    date = models.DateField(blank=True, null=True, verbose_name='Дата договора')

    def __str__(self):
        b ='Договор № ' + str(self.number) + ' c ' + str(self.statement.person)

        return b

    class Meta:
        ordering = ['id']
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Plot(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, verbose_name='Договор')
    number_plot = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер делянки')
    date = models.DateField(blank=True, null=True, verbose_name='Дата?')
    forestry = models.CharField(max_length=50, blank=True, null=True, verbose_name='Лесничество')
    district_forestry = models.CharField(max_length=50, blank=True, null=True, verbose_name='Участковое лесничество')
    tract = models.CharField(max_length=50, blank=True, null=True, verbose_name='Урочище')
    quarter = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартал')
    section = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Выдел')
    chop_type = models.CharField(max_length=20, verbose_name='Вид рубки')
    cost = models.FloatField(blank=True, null=True, verbose_name='Стоимость')

    def __str__(self):
        a = 'Делянка ' + str(self.number_plot) + 'для договра ' + self.contract.__str__() +'с ' + \
        str(self.contract.statement.person)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Делянка'
        verbose_name_plural = '1Делянки'


class WoodSpecies(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, verbose_name='Делянка')
    name_wood_species = models.ForeignKey(Breeds, null=True, on_delete=models.SET_NULL, verbose_name='Подора')


    def __str__(self):
        return str(self.plot.contract.statement.person) + ' ' + str(self.name_wood_species)

    class Meta:
        ordering = ['id']
        verbose_name = 'Порода дерева'
        verbose_name_plural = '2Породы деревьев'


class PlotWoodSpecies(models.Model):
    wood_species = models.ForeignKey(WoodSpecies, on_delete=models.CASCADE, verbose_name='Порода в делянке')
    number_of_trees = models.IntegerField(blank=True, null=True, verbose_name='Количество деревьев')
    large = models.IntegerField(blank=True, null=True, verbose_name='Крупная')
    average = models.IntegerField(blank=True, null=True, verbose_name='Средняя')
    small = models.IntegerField(blank=True, null=True, verbose_name='Мелкая')
    firewood = models.IntegerField(blank=True, null=True, verbose_name='Дровяная')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')

    def __str__(self):
        a = str(self.wood_species.plot.contract.statement.person) + str(self.wood_species.name_wood_species)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Данные по породе'
        verbose_name_plural = '3Данные по породам'
    # number_of_trees количество деревьев
    # large крупная (кубов)
    # average средняя (кубов)
    # small мелкая (кубов)
    # firewood дрова (кубов)
    # unmarketable неликвид (кубов)
    # total всего (кубов)
    # price цена
    # cost стоимость
    # wood species древесная порода
