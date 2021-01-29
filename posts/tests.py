from django.test import TestCase
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setup(self):
        Post.objects.create(text='This is a testing post')
    
    def test_text_content(self):
        post = Post.objects.get(id=2)
        text = f'{post.text}'
        self.assertEqual(text,'This is a testing post')