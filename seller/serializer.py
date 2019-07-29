from rest_framework import serializers

from .models import Seller
from commission.serializer import CommissionSerializer


class SellerSerializer(serializers.ModelSerializer):
    commission_seller = CommissionSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        exclude = ('created_at', 'updated_at',)


