from django.db import models
from plan.models import Plan


class Seller(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=15)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return self.name
