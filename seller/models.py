from django.db import models
from plan.models import Plan


class Seller(models.Model):

    name = models.CharField(blank=False, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=250)
    age = models.IntegerField(blank=False, default=0)
    email = models.EmailField(blank=False, max_length=254)
    cpf = models.CharField(blank=False, max_length=14)
    phone = models.CharField(blank=True, null=True, max_length=15)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, blank=False, related_name='seller_plan')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return self.name
