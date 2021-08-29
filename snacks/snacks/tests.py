from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class thingsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        # url = reverse('contact')
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_templete(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')