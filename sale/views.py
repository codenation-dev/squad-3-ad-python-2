from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializer import SaleSerializer
from .models import Sale
from plan.models import Plan
from seller.models import Seller
from commission.models import Commission
from commi_sales.settings.common import EMAIL_HOST_USER


class SaleViewSet(ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

	@staticmethod
	def calculate_commission(data):
		seller_plan = Plan.objects.get(seller_plan=data['seller'])
		amount = data['amount']
		if amount >= seller_plan.min_value:
			return (seller_plan.upper_percentage / 100) * amount
		else:
			return (seller_plan.lower_percentage / 100) * amount

	@staticmethod
	def create_seller_commission(seller_id, value, month, year):
		seller = Seller.objects.get(id=seller_id)
		data = {
			'value': value,
			'month': month,
			'year': year,
			'seller': seller
		}
		obj, created = Commission.objects.get_or_create(**data)
		return obj.value

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		initial_data = serializer.initial_data
		seller_commission = self.calculate_commission(initial_data)
		commission = self.create_seller_commission(
			initial_data['seller'],
			seller_commission,
			initial_data['month'],
			initial_data['year'],
		)

		serializer.is_valid(raise_exception=True)

		self.perform_create(serializer)  # save
		headers = self.get_success_headers(serializer.data)
		data = {
			'id': serializer.data['seller'],
			'commission': commission
		}
		return Response(data, status=status.HTTP_201_CREATED, headers=headers)


def send_email(email, mean):
	subject = '[Commi Sales] Baixa da média de comissão de vendas'
	from_email = EMAIL_HOST_USER
	message = f"Cuidado! Sua média de comissão dos últimos 5 meses está abaixo do esperado! Média de R$: {mean}"
	send_mail(message=message, subject=subject, from_email=from_email, recipient_list=[email])


@api_view(["POST"])
def check_commission(request):
    data = request.data
    seller = data['seller']
    amount = data['amount']

    sales = Sale.objects.filter(seller__id=seller).order_by('-month')[:5]
    sales = sorted(sales, key=lambda s: s.amount)

    cont = 0
    value_sum = 0
    month_sum = 0
    for s in sales:
        cont += 1
        month_sum += cont
        value_sum = value_sum + cont * s.amount
    mean = float((value_sum/month_sum)) * 0.9

    if float(amount) > mean:
        return Response({"should_notify": False})

    seller_email = Seller.objects.get(pk=seller).email
    send_email(seller_email, mean)
    return Response({"should_notify": True})
