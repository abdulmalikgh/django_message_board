from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
# class PostModelTest(TestCase):
#     def setup(self):
#         Post.objects.create(text='This is a testing post')
    
#     def test_text_content(self):
#         post = Post.objects.get(id=2)
#         text = f'{post.text}'
#         self.assertEqual(text,'This is a testing post')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="This is a testing text")

    def test_url_exist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): 
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'home.html')
