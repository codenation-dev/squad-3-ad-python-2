from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializer import PlanSerializer
from .models import Plan


class PlanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Plan.objects.all()
	lookup_field = 'id'
	serializer_class = PlanSerializer


class PlanListCreateAPIView(ListCreateAPIView):
	queryset = Plan.objects.all()
	serializer_class = PlanSerializer
