from django.db import models
from core.models.workers import Worker


class District(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    mefakeah = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='districts',
    )

    def __str__(self):
        return self.name
