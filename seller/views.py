from operator import itemgetter

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Q

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
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def list(self, request, *args, **kwargs):
        data = self.filter_sellers(**kwargs)
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
    def get_sum_commission_seller(commissions, year, month):
        commissions_filtered = filter(
            lambda commission: commission['month'] == month and commission['year'] == year, commissions
        )
        return sum(commission['value'] for commission in commissions_filtered)

    def response_sellers(self, sellers, month, year):
        response = []
        for seller in sellers:
            sum_commission_sellers = self.get_sum_commission_seller(seller['commission_seller'], month, year)
            response.append({
                'name': seller['name'],
                'id': seller['id'],
                'max_commission': sum_commission_sellers,
            })
        return response

    def filter_sellers(self, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')

        sellers_with_commissions = Seller.objects.filter(commission_seller__year=year, commission_seller__month=month)
        sellers_without_commissions = Seller.objects.filter(
            ~Q(commission_seller__year=year, commission_seller__month=month)
        )
        serializer_with_commissions = self.get_serializer(sellers_with_commissions, many=True)
        serializer_without_commissions = self.get_serializer(sellers_without_commissions, many=True)

        response = self.response_sellers(serializer_with_commissions.data, year, month)
        response.extend(self.response_sellers(serializer_without_commissions.data, year, month))

        unique_response = {v['id']: v for v in response}.values()
        return sorted(unique_response, key=itemgetter('max_commission'), reverse=True)
