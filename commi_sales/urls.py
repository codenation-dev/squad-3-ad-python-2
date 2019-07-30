from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from django.urls import path
from rest_framework import routers

from plan.views import PlanViewSet
from sale.views import SaleViewSet, CheckCommissionApiView
from seller.views import SellerViewSet, ListSellersByCommissionAPIView


router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('check_commission/', CheckCommissionApiView.as_view(), name='check_commission'),
	path('', include_docs_urls(title='Commi Sales API', description='Documentation')),
	path(
		'list_by_commission/<int:commission_seller__month>/<int:commission_seller__year>',
		ListSellersByCommissionAPIView.as_view(),
		name='list_by_commission'
	)
]

urlpatterns.extend(router.urls)
