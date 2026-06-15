from django.db import models


class KindOfWater(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class KindOfArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class KindOfJob(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class KindOfNeighborhood(models.Model):
    name = models.CharField(max_length=100)

    # Each neighborhood belongs to exactly one district
    district = models.ForeignKey(
        'core.District',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='neighborhoods',
    )

    def __str__(self):
        return self.name
