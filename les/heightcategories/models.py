from django.db import models


class Fff(models.Model):
    diametrs = models.CharField(max_length=20, verbose_name='Диаметр', default='')

    class Meta:
        verbose_name = 'Диаметр'
        verbose_name_plural = 'Диаметры'

