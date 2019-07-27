from django.urls import path

from .views import check_comission


urlpatterns = [
    path('check_comission/', check_comission, name='check_comission'),
]
