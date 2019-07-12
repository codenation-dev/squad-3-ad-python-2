from django.db import models


class Plan(models.Model):

    name = models.CharField(max_length=100)
    minimum_value = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_percentage = models.FloatField()
    maximum_percentage = models.FloatField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return f'{self.minimum_value}'
