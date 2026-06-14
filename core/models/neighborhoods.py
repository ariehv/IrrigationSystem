from django.db import models
from core.models.workers import Worker
from core.models.districts import District


class District(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    kablan = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='districts',
    )
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='neighborhoods',
    )

    def __str__(self):
        return self.name
