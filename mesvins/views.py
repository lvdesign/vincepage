from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Vin 
# Create your views here.


class VinListView(ListView):
    model = Vin 
    template_name = 'home.html'


class VinDetailView(DetailView):
    model = Vin 
    template_name = 'vin_detail.html'


class VinCreateView(CreateView):
    model = Vin 
    template_name='vin_new.html'
    fields=['name', 'author', 'description']

class VinUpdateView(UpdateView):
    model = Vin 
    template_name='vin_edit.html'
    fields=['name', 'description']


class VinDeleteView(DeleteView):
    model = Vin 
    template_name='vin_delete.html'
    success_url = reverse_lazy('home')