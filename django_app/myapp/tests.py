from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class DjangoAppTestCase(TestCase):
    def test_hello_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello, world!")
