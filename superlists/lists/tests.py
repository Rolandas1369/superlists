from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_page_(self):
        # built in client usage
        response = self.client.get('/')
        # django built assert
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # readable format
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    # this way we are posting to '/' path data={'item_text': 'A new list item'}
    def test_can_save_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        # checks if 'A new list item' in response
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
