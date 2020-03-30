from django.urls import resolve
from django.test import TestCase
from .views import home_page
from django.http import HttpRequest
import pprint
# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_home_page_(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        # built in client usage
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    # this way we are posting to / data={'item_text': 'A new list item'}
    def test_can_save_POST_request(self):

        response = self.client.post('/', data={'item_text': 'A new list item'})
        print(str(response.content.decode()))
        # checks if 'A new list item' in response
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
