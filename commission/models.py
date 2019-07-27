from django.db import models


class Plan(models.Model):

    min_value = models.DecimalField(max_digits=10, decimal_places=2)
    lower_percentage = models.FloatField()
    upper_percentage = models.FloatField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return f'{self.min_value}'


class Commission(models.Model):
    commission = models.FloatField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return f'{self.commission}'
