from rest_framework import serializers

from .models import Plan, Commission


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        exclude = ('created_at', 'updated_at',)


class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        exclude = ('created_at', 'updated_at',)
