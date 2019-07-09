from django.db import models


class Plan(models.Model):

    name = models.CharField(max_length=100)
    minimum_value = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_percentage = models.FloatField()
    maximum_percentage = models.FloatField()

    def __str__(self):
        return f'{self.minimum_value}'
