from django.test import TestCase
from .models import *

# Create your tests here.

class ImageTestCase(TestCase):
    def setUp(self):
        """image creation
        """
        user = User.objects.create(
            username = 'nashlil',
            first_name = 'lilian',
            last_name = 'kanana')
        
        Image.objects.create(
            name="me",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )
    def test_image_name(self):
        """tests image name
        """
        image=Image.objects.get(name="me")
        self.assertEqual(image.name, "me")
