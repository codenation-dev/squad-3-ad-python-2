from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializer import SellerSerializer
from .models import Seller


class SellerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Seller.objects.all()
	lookup_field = 'id'
	serializer_class = SellerSerializer


class SellerListCreateAPIView(ListCreateAPIView):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer
