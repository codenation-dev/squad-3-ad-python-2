from rest_framework import serializers

from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('created_at', 'updated_at',)
