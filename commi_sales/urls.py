from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from commission.views import PlanViewSet
from sale.views import SaleViewSet
from seller.views import SellerViewSet

schema_view = get_swagger_view(title='API Documentation')
urlpatterns = [path('admin/', admin.site.urls), url(r'^$', schema_view)]

router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns.extend(router.urls)

