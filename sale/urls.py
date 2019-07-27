from django.urls import path

from .views import check_commission


urlpatterns = [
    path('check_commission/', check_commission, name='check_commission'),
]
