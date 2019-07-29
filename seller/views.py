from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .serializer import SellerSerializer
from .models import Seller
from commission.serializer import CommissionSerializer
from commission.models import Commission


class SellerViewSet(ModelViewSet):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

	def retrieve(self, request, *args, **kwargs):
		obj = self.get_object()
		serializer = self.get_serializer(obj)
		data = serializer.data
		response = {
			'name': data['name'],
			'id': data['id'],
			'commissions': data['commission_seller'],
		}
		return Response(response)

	def list(self, request, *args, **kwargs):
		serializer = self.get_serializer(self.queryset, many=True)
		data = serializer.data
		response = [
			{
				'name': d['name'],
				'id': d['id'],
				'commissions': data['commission_seller'],
			}
			for d in data
		]
		return Response(response)


class SellerOrderedByComission(ListAPIView):
    	
	lookup_url_kwarg = ['year','month']
	serializer_class = CommissionSerializer

	def get_queryset(self):		
		year, month = self.kwargs.get(self.lookup_url_kwarg)
		compensations = Comission.objects.filter(year=year).filter(month=month).order_by('value')
		sellers = []
		for compensation in compensations:
			sellers.append(compensation.seller)

		return sellers

