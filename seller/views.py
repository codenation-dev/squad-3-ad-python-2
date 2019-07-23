from rest_framework.viewsets import ModelViewSet

from .serializer import SellerSerializer
from .models import Seller


class SellerViewSet(ModelViewSet):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

