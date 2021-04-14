# mesvins/urls.py
from django.urls import path
from .views import VinListView, VinDetailView



urlpatterns = [
    path('vin/<int:pk>/', VinDetailView.as_view(), name='vin_detail'),
    path('', VinListView.as_view(), name='home'),
]