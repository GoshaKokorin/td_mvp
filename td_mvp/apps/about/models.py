from django.db import models


class About(models.Model):
    name = models.CharField('Название', max_length=64)
    value = models.CharField('Значение', max_length=64)
    position = models.PositiveSmallIntegerField('Позиция', default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизит'
        ordering = ['position']

    def __str__(self):
        return self.name


class Geo(models.Model):
    lat = models.FloatField()
    log = models.FloatField()

    class Meta:
        verbose_name = 'Геопозиции'
        verbose_name_plural = 'Геопозиция'
