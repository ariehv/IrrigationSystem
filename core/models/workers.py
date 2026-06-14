from django.db import models
from core.models.lookups import KindOfJob


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    job = models.ForeignKey(
        'lookups.KindOfJob',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workers',
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"