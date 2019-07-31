from operator import itemgetter

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view

from .serializer import SellerSerializer
from .models import Seller
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
        data = self.get_queryset(**kwargs)
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
    def get_sum_commission_seller(commissions, month, year):
        commissions_filtered = [
            commission for commission in commissions \
            if commission['month'] == month and commission['year'] == year
        ]
        if commissions_filtered:
            return sum(commission['value'] for commission in commissions_filtered)
        return commissions_filtered

    def get_queryset(self, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')

        sellers_with_commissions = Seller.objects.filter(commission_seller__year=year, commission_seller__month=month)
        sellers_without_commissions = Seller.objects.filter(
            ~Q(commission_seller__year=year, commission_seller__month=month)
        )
        serializer_with_commissions = self.get_serializer(sellers_with_commissions, many=True)
        serializer_without_commissions = self.get_serializer(sellers_without_commissions, many=True)

        response = []
        for seller in serializer_with_commissions.data:
            response.append({
                'name': seller['name'],
                'id': seller['id'],
                'max_commission': self.get_sum_commission_seller(seller['commission_seller'], month, year),
            })

        for seller in serializer_without_commissions.data:
            response.append({
                'name': seller['name'],
                'id': seller['id'],
                'max_commission': 0
            })

        unique_response = {v['id']: v for v in response}.values()
        return sorted(unique_response, key=itemgetter('max_commission'), reverse=True)

