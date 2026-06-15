from django.db import models
from core.models.lookups import KindOfArea, KindOfNeighborhood


class Area(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    kind_of_area = models.ForeignKey(
        KindOfArea,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='areas',
    )

    kind_of_neighborhood = models.ForeignKey(
        KindOfNeighborhood,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='areas',
    )

    def __str__(self):
        return self.name
