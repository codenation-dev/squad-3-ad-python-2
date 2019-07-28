from rest_framework import serializers

from .models import Commission


class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        exclude = ('created_at', 'updated_at')
