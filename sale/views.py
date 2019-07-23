from rest_framework.viewsets import ModelViewSet

from .serializer import SaleSerializer
from .models import Sale


class SaleViewSet(ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer
