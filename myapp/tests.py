import imp
from django.test import TestCase
from .models import Posts
from django.urls import reverse

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Posts.objects.create(text="ini adalah text")

    
    def test_text_content(self):
        post=Posts.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'ini adalah text')



class HomePageViewTest(TestCase):

    def setUp(self):
        Posts.objects.create(text='apakah ini juga text')

    
    def test_view_url_exits_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')