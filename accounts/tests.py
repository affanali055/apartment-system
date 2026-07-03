from django.test import TestCase


class AccountsSanityTest(TestCase):
    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertIn(response.status_code, (200, 302))
