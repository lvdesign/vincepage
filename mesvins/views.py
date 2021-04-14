from django.views.generic import ListView, DetailView

from . models import Vin 
# Create your views here.


class VinListView(ListView):
    model = Vin 
    template_name = 'home.html'


class VinDetailView(DetailView):
    model = Vin 
    template_name = 'vin_detail.html'