from django.db import models
from core.models.lookups import KindOfWater


class Meter(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    mispar_mone = models.CharField(max_length=100, unique=True)

    kind_of_water = models.ForeignKey(
        KindOfWater,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='meters',
    )

    def __str__(self):
        return f"Meter {self.mispar_mone}"
