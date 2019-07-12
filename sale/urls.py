from django.urls import path

from .views import SaleListCreateAPIView, SaleRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', SaleListCreateAPIView.as_view(), name='sale_list_create'),
    path('<id>', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale_retrieve_update_destroy'),
]
