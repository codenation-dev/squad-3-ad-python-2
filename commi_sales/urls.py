from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from django.urls import path
from rest_framework import routers

from plan.views import PlanViewSet
from sale.views import SaleViewSet, check_commission
from seller.views import SellerViewSet
from commission.views import CommissionViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Commi-Sales')
urlpatterns = [
	path('admin/', admin.site.urls),
	path('check_commission/', check_commission, name='check_commission'),
	#path('seller/<int:year>/<int:month>/', SellerOrderedByComission.as_view(),name='ordered_sellers'),
	path('', include_docs_urls(title='Commi Sales API', description='Documentation'))
]

router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'comission', CommissionViewSet)

urlpatterns.extend(router.urls)
