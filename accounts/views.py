from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




'''
Why use reverse_lazy here instead of reverse ? 
The reason is that for all generic class-based
views the URLs are not loaded when the file is imported, 
so we have to use the lazy form of reverse 
to load them later when they’re available.

'''