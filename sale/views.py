from rest_framework.viewsets import ModelViewSet

from .serializer import SaleSerializer
from .models import Sale
from seller.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SaleViewSet(ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer


def send_email(email):

    remetente = 'squad3python@gmail.com'
    senha = ''
    destinatario = [email]
    assunto = 'Check Comission'
    msg = MIMEMultipart('alternative')
    texto = "Sua média de comissão dos últimos 5 meses está abaixo do esperado!"
    part1 = MIMEText(texto, 'plain')

    msg.attach(part1)

    msg = '\r\n'.join(['From: %s' % remetente, 'To: %s' % destinatario,\
		'Subject: %s' % assunto, '', '%s' % texto]).encode('UTF-8')

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, msg)
    server.quit()


@api_view(["POST"])
def check_commission(request):

	data = request.data
	seller = data['seller']
	amount = data['amount']

	sale = Sale.objects.filter(seller__id=seller).order_by('amount')[:5]
	cont = 0
	total = 0
	soma = 0
	for s in sale:
		cont = cont + 1
		soma = soma + cont
		total = total + cont * s.amount
	media = float((total/soma)) * 0.9

	if media < float(amount):
		return Response({"should_notify": False})
	else:	
		seller_email = Seller.objects.filter(pk=seller).values('email')
		email = seller_email[0]['email']
		send_email(email)
		return Response({"should_notify": True})
