from django.db import models
from seller.models import Seller


class Sale(models.Model):

    sale_value = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    month = models.DateField()


    def __str__(self):
        return f'{self.month}'
