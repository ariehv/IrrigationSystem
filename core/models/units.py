from django.db import models
from core.models.areas import Area
from core.models.meters import Meter


class IrrigationUnit(models.Model):
    number_comp = models.CharField(max_length=100)
    operator = models.CharField(max_length=100, blank=True, null=True)
    coordinates = models.CharField(max_length=100, blank=True, null=True)

    area = models.ForeignKey(
        Area,
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
        return f"Unit {self.number_comp}"
