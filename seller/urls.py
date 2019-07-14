from django.urls import path

from .views import SellerListCreateAPIView, SellerRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', SellerListCreateAPIView.as_view(), name='seller_list_create'),
    path('<id>', SellerRetrieveUpdateDestroyAPIView.as_view(), name='seller_retrieve_update_destroy'),
]
