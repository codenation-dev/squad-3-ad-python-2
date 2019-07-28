from rest_framework import serializers

from plan.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        exclude = ('created_at', 'updated_at',)

