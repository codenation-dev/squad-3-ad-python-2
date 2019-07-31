from unittest import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from seller.models import Seller
from sale.models import Sale
from plan.models import Plan
from .views import ListSellersByCommissionAPIView


class TestSellerViewSet(TestCase):

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

	def test_retrieve(self):
		response = self.client.get(reverse('seller-detail', kwargs={'pk': self.seller.id}))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(self.seller.name, "Test Seller")

	def test_list(self):
		response = self.client.get(reverse('seller-list'))
		self.assertEqual(response.status_code, 200)
		assert isinstance(response.data, list)
		assert isinstance(response.data[0]['commissions'], list)


class TestListSellersByCommissionAPIView(TestCase):

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
		data_sale = {
			'amount': 10000,
			'year': 2019,
			'month': 2,
			'seller': self.seller
		}
		self.sale = Sale.objects.create(**data_sale)
		self.client = APIClient()

	def test_list(self):
		response = self.client.get(
			reverse('ordered_sellers', kwargs={'year': 2019, 'month': 2})
		)
		self.assertEqual(response.status_code, 200)

	def test_get_sum_commission_seller(self):
		commissions = [
			{
				"value": 37,
				"month": 2,
				"year": 2019
			},
			{
				"value": 3,
				"month": 2,
				"year": 2019
			}
		]
		response = ListSellersByCommissionAPIView().get_sum_commission_seller(commissions, 2019, 2)
		self.assertEqual(response, 40)
