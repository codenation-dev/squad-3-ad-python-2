from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
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

@api_view(["GET"])
def get_ordered_by_comission(self, request, *args, **kwargs):
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

