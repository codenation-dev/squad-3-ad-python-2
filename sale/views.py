import smtplib
from email.mime.multipart import MIMEMultipart
from rest_framework.decorators import api_view
from rest_framework.response import Response
from email.mime.text import MIMEText
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializer import SaleSerializer
from .models import Sale
from plan.models import Plan
from seller.models import Seller
from commission.models import Commission


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
	def create_seller_commission(seller_id, value, month):
		seller = Seller.objects.get(id=seller_id)
		data = {
			'value': value,
			'month': month,
			'seller': seller
		}
		obj, created = Commission.objects.get_or_create(**data)
		return obj.value

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		initial_data = serializer.initial_data
		seller_commission = self.calculate_commission(initial_data)
		commission = self.create_seller_commission(initial_data['seller'], seller_commission, initial_data['month'])

		serializer.is_valid(raise_exception=True)

		self.perform_create(serializer)  # save
		headers = self.get_success_headers(serializer.data)
		data = {
			'id': serializer.data['seller'],
			'commission': commission
		}
		return Response(data, status=status.HTTP_201_CREATED, headers=headers)

def send_email(email, mean):

    from_email = 'squad3python@gmail.com'
    password = 'gvpqohbfgkjcickw'
    to = [email]
    title = 'Check Comission'
    msg = MIMEMultipart('alternative')
    text = f"Sua média de comissão dos últimos 5 meses está abaixo do esperado! Média de R$: {mean}"
    part1 = MIMEText(text, 'plain')

    msg.attach(part1)

    msg = '\r\n'.join(['From: %s' % from_email, 'To: %s' % to,\
		'Subject: %s' % title, '', '%s' % text]).encode('UTF-8')

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to, msg)
    server.quit()

@api_view(["POST"])
def check_comission(request):

	data = request.data
	seller = data['seller']
	amount = data['amount']

	sales = Sale.objects.filter(seller__id=seller).order_by('-month')[:5]
	sales = sorted(sales, key=lambda s: s.amount)

	cont = 0
	value_sum = 0
	month_sum  = 0
	for s in sales:
		cont += 1
		month_sum += cont
		value_sum = value_sum + cont * s.amount
	mean = float((value_sum/month_sum)) * 0.9

	if mean < float(amount):
		return Response({"should_notify": False})
	else:	
		seller_email = Seller.objects.filter(pk=seller).values('email')
		email = seller_email[0]['email']
		send_email(email, mean)
		return Response({"should_notify": True})

	return Response({"resposta": "teste"})
