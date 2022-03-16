from django.db import models


class Diameter(models.Model):
    name = models.CharField(max_length=20, verbose_name='Диаметр')

    class Meta:
        verbose_name = 'Диаметр'
        verbose_name_plural = 'Диаметры'
