from rest_framework.viewsets import ModelViewSet

from .serializer import PlanSerializer
from .models import Plan


class PlanViewSet(ModelViewSet):
	queryset = Plan.objects.all()
	serializer_class = PlanSerializer
