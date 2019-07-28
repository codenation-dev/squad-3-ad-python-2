from django.db import models

from seller.models import Seller


class Commission(models.Model):

    value = models.FloatField()
    month = models.IntegerField()
    year = models.IntegerField()
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        blank=False,
        related_name='commission_seller'
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return f'{self.value}'
