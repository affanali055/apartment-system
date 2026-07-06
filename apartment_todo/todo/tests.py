from django.test import SimpleTestCase
from django.urls import reverse


class TodoPageTests(SimpleTestCase):
    def test_todo_page_loads(self):
        response = self.client.get(reverse('todo_page'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Todo Management')
