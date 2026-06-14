from django.db import models


class KindOfOperator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
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
