from django.urls import path

from .views import PlanListCreateAPIView, PlanRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', PlanListCreateAPIView.as_view(), name='plan_list_create'),
    path('<id>', PlanRetrieveUpdateDestroyAPIView.as_view(), name='plan_retrieve_update_destroy'),
]
