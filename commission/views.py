from rest_framework.viewsets import ModelViewSet

from .serializer import CommissionSerializer, PlanSerializer
from .models import Commission, Plan


class CommissionViewSet(ModelViewSet):
	queryset = Commission.objects.all()
	serializer_class = CommissionSerializer


class PlanViewSet(ModelViewSet):
	queryset = Plan.objects.all()
	serializer_class = PlanSerializer
