from operator import itemgetter

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializer import SellerSerializer
from .models import Seller


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

	def get_queryset(self):
		return self.queryset

	def list(self, request, *args, **kwargs):
		serializer = self.get_serializer(self.queryset, many=True)
		data = serializer.data
		response = [
			{
				'name': d['name'],
				'id': d['id'],
				'commissions': d['commission_seller'],
			}
			for d in data
		]
		return Response(response)


class ListSellersByCommissionAPIView(ListAPIView):
	serializer_class = SellerSerializer

	def list(self, request, *args, **kwargs):
		data = self.filter_queryset(self.get_queryset(**kwargs))
		response = [
			{
				'name': d['name'],
				'id': d['id'],
				'commission': d['max_commission'],
			}
			for d in data
		]
		return Response(response)

	@staticmethod
	def get_max_commission_seller(commissions, month, year):
		commissions_filtered = [
			commission for commission in commissions \
			if commission['month'] == month and commission['year'] == year
		]
		if commissions_filtered:
			return sum(commission['value'] for commission in commissions_filtered)
		return commissions_filtered

	def get_queryset(self, **kwargs):
		sellers_with_commissions = Seller.objects.filter(**kwargs)
		serializer = self.get_serializer(sellers_with_commissions, many=True)
		response = []
		for seller in serializer.data:
			response.append({
				'name': seller['name'],
				'id': seller['id'],
				'max_commission': self.get_max_commission_seller(
					seller['commission_seller'],
					kwargs.get('commission_seller__month'),
					kwargs.get('commission_seller__year'),
				),
			})
		unique_response = {v['id']: v for v in response}.values()
		return sorted(unique_response, key=itemgetter('max_commission'), reverse=True)
