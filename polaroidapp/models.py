from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/')
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    uploaded_image = models.ImageField(upload_to = 'uploads/')
    image_name = models.CharField(max_length=30)
    caption = models.TextField()
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE) 

class Comment(models.Model):
    comment = models.TextField()
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Likes(models.Model):
    likes = models.IntegerField(default=0)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE) 