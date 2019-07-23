from rest_framework import routers
from django.contrib import admin
from django.urls import path

from plan.views import PlanViewSet
from sale.views import SaleViewSet
from seller.views import SellerViewSet


urlpatterns = [path('admin/', admin.site.urls)]

router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns.extend(router.urls)

