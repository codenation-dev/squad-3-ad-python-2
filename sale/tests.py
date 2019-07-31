from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse

from plan.models import Plan
from seller.models import Seller
from commission.models import Commission


class TestSaleViewSet(APITestCase):

    def setUp(self):
        self.plan = Plan.objects.create(min_value=15000, lower_percentage=5, upper_percentage=15)
        data_seller = {
            'name': "Test Seller",
            'age': 20,
            'email': "test_seller@gmail.com",
            'cpf': "123456789",
            'plan': self.plan,
        }
        self.seller = Seller.objects.create(**data_seller)
        self.client = APIClient()

    def test_create(self):
        url = reverse('sale-list')
        data = {
            'amount': 10000,
            'year': 2019,
            'month': 2,
            'seller': self.seller.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        commission = Commission.objects.filter(pk=1)[0]
        self.assertEqual(commission.value,500)  #verifies if the created commission was calculated correctly and stored properly


class TestCheckCommissionApiView(APITestCase):

    def setUp(self):
        self.url = reverse('check_commission')
        self.client = APIClient()

    def test_post(self):
        data = {"seller": 10, "amount": 1000.65}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
