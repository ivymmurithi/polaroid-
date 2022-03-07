from django.test import TestCase

from polaroidapp.views import likes
from .models import Profile,Image,Comment

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.profile1= Profile(bio= 'this is a cat')
        self.profile1.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile1,Profile))

    def test_save_method(self):
        self.profile1.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile1.save_profile()
        self.profile1.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) -1)

class ImageTestClass(TestCase):

    def setUp(self):
        self.image1= Image(image_name= 'Cat', caption='This is a cat', likes=1)
        self.image1.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

    def test_save_method(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image1.save_image()
        self.image1.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) -1)