from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from django.urls import path
from rest_framework import routers

from plan.views import PlanViewSet
from sale.views import SaleViewSet, CheckCommissionApiView
from seller.views import SellerViewSet, ListSellersByCommissionAPIView
from commission.views import CommissionViewSet


router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'comission', CommissionViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('check_commission/', CheckCommissionApiView.as_view(), name='check_commission'),
	path('', include_docs_urls(title='Commi Sales API', description='Documentation')),
	path('sellers/<int:year>/<int:month>/', ListSellersByCommissionAPIView.as_view(), name='ordered_sellers')
]

urlpatterns.extend(router.urls)
