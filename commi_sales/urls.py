from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from django.urls import path
from rest_framework import routers

from plan.views import PlanViewSet
from sale.views import SaleViewSet
from seller.views import SellerViewSet


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include_docs_urls(title='Commi Sales API', description='Documentation'))
]

router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns.extend(router.urls)
