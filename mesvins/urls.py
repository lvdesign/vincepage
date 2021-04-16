# mesvins/urls.py
from django.urls import path
from .views import VinListView, VinDetailView, VinCreateView, VinUpdateView, VinDeleteView



urlpatterns = [
    path('vin/<int:pk>/delete/', VinDeleteView.as_view(), name='vin_delete'),
    path('vin/<int:pk>/edit/', VinUpdateView.as_view(), name='vin_edit'),
    path('vin/new/', VinCreateView.as_view(), name='vin_new'),
    path('vin/<int:pk>/', VinDetailView.as_view(), name='vin_detail'),
    path('', VinListView.as_view(), name='home'),
]