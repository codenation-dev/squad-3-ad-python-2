from rest_framework import serializers

from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        exclude = ('created_at', 'updated_at',)
