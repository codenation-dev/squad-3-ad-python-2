from django.db import models
from seller.models import Seller


class Address(models.Model):

    street = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Útima atualização', auto_now=True)

    def __str__(self):
        return self.street
