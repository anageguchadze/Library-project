from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, RequestsClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class AuthorTests(TestCase):
    def setUp(self):
        self.client = APIClient()


    def test_list_authors(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        response = self.client.post(reverse('author-list'), {'name': 'Jack London', 'nationality': 'American'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class BookListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testuser123')
        self.token = RefreshToken.for_user(self.user)

    def test_list_books_unauth(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_books_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookListTestsWithRequestClient(TestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.user = User.objects.create_user(username='testuser123', password='testuser123')
        self.token = RefreshToken.for_user(self.user)
        self.client.headers.update(f'Authorization: Bearer {self.token.access_token}')

