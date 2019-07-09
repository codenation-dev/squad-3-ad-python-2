from django.db import models
from plan.models import *


class Seller(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=15)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


    def __str__(self):
        return self.name