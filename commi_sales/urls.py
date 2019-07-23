from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('sales/', include(('sale.urls', 'sale'), namespace='sales')),
    path('sellers/', include(('seller.urls', 'seller'), namespace='sellers')),
    path('plans/', include(('plan.urls', 'plan'), namespace='plans')),
    path('admin/', admin.site.urls)
]
