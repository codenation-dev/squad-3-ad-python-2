from django.test import TestCase
from rest_framework.test import APIRequestFactory


class TestSaleViewSet(TestCase):
	factory = APIRequestFactory()

	def test_create(self):
		data = {
			"amount": 10000,
			"month": 2,
			"seller": 1
		}
		response = self.factory.post('/sales/', data, format='json')
