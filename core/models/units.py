from django.db import models
from core.models.lookups import KindOfOperator, KindOfArea
from core.models.meters import Meter


class IrrigationUnit(models.Model):
    num_green=models.CharField(max_length=100, blank=True, null=True)
    number_comp = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    year_established = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    operator = models.ForeignKey(
        'lookups.KindOfOperator',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='irrigation_units',
    )
    

    area = models.ForeignKey(
        'lookups.KindOfArea',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='irrigation_units',
    )

    meter = models.ForeignKey(
        Meter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='irrigation_units',
    )

    def __str__(self):
        return f"Unit {self.num_green}"
