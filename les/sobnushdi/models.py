from django.db import models

from person.models import Person


class Tract(models.Model):#Урочище
    name = models.CharField(max_length=100, verbose_name='Урочище')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Урочище'
        verbose_name_plural = 'Урочища'


class Forestry(models.Model):#Лесничесвто
    name = models.CharField(max_length=100, verbose_name='Лесничество')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Лесничество'
        verbose_name_plural = 'Лесничества'


class DistrictForestry(models.Model):
    name = models.CharField(max_length=100, verbose_name='Участковое лесничество')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Участковое лесничество'
        verbose_name_plural = 'Участковые лесничества'


class Breed(models.Model): #Порода
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название породы')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class HeatedPremise(models.Model):# Отапливаемое помещение
    cadastral_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Кадастровый номер')
    postcode = models.CharField(max_length=6, blank=True, null=True,default='646350', verbose_name='Индекс')
    region = models.CharField(max_length=100, blank=True, null=True, default='Омская', verbose_name='Область')
    district = models.CharField(max_length=50, blank=True, null=True, default='Колосовский', verbose_name='Район')
    locality = models.CharField(max_length=50, blank=True, null=True,default='Колосовка', verbose_name='Населенный пункт')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Дом')
    apartment_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартира')

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
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='ФИО')
    number_statement = models.PositiveSmallIntegerField(verbose_name='Номер заявления')
    date = models.DateField(blank=True, null=True, verbose_name='Дата заявления')
    heated_promise = models.OneToOneField(HeatedPremise, on_delete=models.SET_NULL, blank=True,
                                          null=True, verbose_name='Адрес отапливаемого помещения')
    there_is_a_contract = models.BooleanField(editable=False, verbose_name='Есть договор', default=False)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество по заявлению')
    refusal_to_conclude_a_contract = models.BooleanField(verbose_name='Отказ', default=False)

    def __str__(self):
        num = str(self.number_statement)
        data = str(self.date)
        #fio = str(self.person)
        a = str('№  ' + num + ' от ' + data)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class PlotWoodSpecies(models.Model): #Количество-качество по породе
    name = models.ForeignKey(Breed, on_delete=models.DO_NOTHING, verbose_name='Порода')
    number_of_trees = models.IntegerField(blank=True, null=True, verbose_name='Количество деревьев')
    large = models.IntegerField(blank=True, null=True, verbose_name='Крупная')
    average = models.IntegerField(blank=True, null=True, verbose_name='Средняя')
    small = models.IntegerField(blank=True, null=True, verbose_name='Мелкая')
    firewood = models.IntegerField(blank=True, null=True, verbose_name='Дровяная')
    brushwood = models.IntegerField(blank=True, null=True, verbose_name='Хворост(неликвид)')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')

    def __str__(self):
        a = str(self.name.name)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Данные по породе'
        verbose_name_plural = 'Данные по породам'


class Plot(models.Model): #ДЕЛЯНКА
    number_plot = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер делянки')
    area = models.FloatField(blank=True, null=True, verbose_name='Площадь')
    forestry = models.ForeignKey(Forestry, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Лесничество')
    district_forestry = models.ForeignKey(DistrictForestry, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Участковое лесничество')
    tract = models.ForeignKey(Tract, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Урочище')
    quarter = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Квартал')
    section = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Выдел')
    chop_type = models.CharField(blank=True, null=True, max_length=100, default='рубка спелых и перестойных лесных насаждений', verbose_name='Вид рубки')
    type_of_forestry = models.CharField(blank=True, null=True, max_length=100, default='мягколиственное', verbose_name='Хозяйство')
    cost = models.FloatField(blank=True, null=True, verbose_name='Стоимость')
    cost_in_words = models.FloatField(blank=True, null=True, verbose_name='Стоимость прописью')
    plot_wood_species = models.ManyToManyField(PlotWoodSpecies, blank=True, verbose_name='Данные по породе')

    def __str__(self):
        a = 'Делянка ' + str(self.number_plot)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Делянка'
        verbose_name_plural = 'Делянки'


class Contract(models.Model):
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE, verbose_name='Заявление')
    number_decree = models.CharField(max_length=7, verbose_name='номер распоряжения')
    date_decree = models.DateField(blank=True, null=True, verbose_name='дата распоряжения')
    number = models.CharField(max_length=7, blank=True, null=True, verbose_name='номер договора')
    date = models.DateField(blank=True, null=True, verbose_name='Дата договора')
    plot = models.OneToOneField(Plot, on_delete=models.CASCADE, verbose_name='Делянка')

    def __str__(self):
        b = 'Договор № ' + str(self.number)
        return b

    class Meta:
        ordering = ['id']
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
