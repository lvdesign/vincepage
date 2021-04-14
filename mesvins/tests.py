# mesvins/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Vin




class MesVinsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.vin = Vin.objects.create(
            name='A good title',
            description='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        vin = Vin(name='A sample title')
        self.assertEqual(str(vin), vin.name)

    def test_vin_content(self):
        self.assertEqual(f'{self.vin.name}', 'A good title')
        self.assertEqual(f'{self.vin.author}', 'testuser')
        self.assertEqual(f'{self.vin.description}', 'Nice body content')

    def test_vin_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_vin_detail_view(self):
        response = self.client.get('/vin/1/')
        no_response = self.client.get('/vin/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'vin_detail.html')