from django.urls import path

from .views import SaleListCreateAPIView, SaleRetrieveUpdateDestroyAPIView, check_comission


urlpatterns = [
    path('', SaleListCreateAPIView.as_view(), name='sale_list_create'),
    path('<id>', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale_retrieve_update_destroy'),
    path('check_comission/', check_comission, name='check_comission'),
]
