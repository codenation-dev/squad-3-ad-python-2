from django.db import models
from seller.models import Seller


class Sale(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return f'{self.month}'
