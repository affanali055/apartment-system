from django.contrib.auth.models import User
from django.test import TestCase


class AccountsSanityTest(TestCase):
    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertIn(response.status_code, (200, 302))

    def test_register_app_url(self):
        response = self.client.get('/register/')
        self.assertIn(response.status_code, (200, 302))

    def test_todo_app_url(self):
        response = self.client.get('/todo/')
        self.assertIn(response.status_code, (200, 302))

    def test_login_redirects_to_todo_page(self):
        User.objects.create_user(username='demo', password='secret123')

        response = self.client.post('/', {'username': 'demo', 'password': 'secret123'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/todo/')
