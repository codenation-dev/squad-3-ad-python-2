from django.db import models
from commission.models import Commission


class Seller(models.Model):

    name = models.CharField(blank=False, max_length=200)
    address = models.CharField(blank=True, max_length=250)
    age = models.IntegerField(blank=False, default=0)
    email = models.EmailField(blank=False, max_length=254)
    cpf = models.CharField(blank=False, max_length=14)
    phone = models.CharField(max_length=15)
    commission_plan = models.ForeignKey(Commission, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return self.name
