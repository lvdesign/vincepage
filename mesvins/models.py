from django.db import models
from django.urls import reverse

# Create your models here.
class Vin(models.Model):
    name = models.CharField(max_length=240)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)

    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vin_detail', args=[str(self.id)])


