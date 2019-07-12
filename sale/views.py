from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializer import SaleSerializer
from .models import Sale


class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Sale.objects.all()
	lookup_field = 'id'
	serializer_class = SaleSerializer


class SaleListCreateAPIView(ListCreateAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer
