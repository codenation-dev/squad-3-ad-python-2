from django.db import models


class Plan(models.Model):

    min_value = models.FloatField()
    lower_percentage = models.FloatField()
    upper_percentage = models.FloatField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return f'{self.min_value}'
