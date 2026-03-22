from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class TestAuthentication(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="pass123"
        )
        self.register_url = reverse('users')
        self.login_url = reverse('login')

    def test__register_new_user(self):
        data = {
            'username': 'testuser1',
            'password': 'pass123',
        }

        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__login_user(self):
        data = {
            'username': 'testuser',
            'password': 'pass123',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
