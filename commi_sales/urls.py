from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers

from plan.views import PlanViewSet
from sale.views import SaleViewSet
from seller.views import SellerViewSet

schema_view = get_swagger_view(title='API Documentation')
urlpatterns = [path('admin/', admin.site.urls), path('', schema_view)]

router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns.extend(router.urls)

