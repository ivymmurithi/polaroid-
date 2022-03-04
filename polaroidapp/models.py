from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    bio = models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Image(models.Model):
    uploaded_image = models.ImageField(upload_to = 'uploads/', null=True)
    image_name = models.CharField(max_length=30, null=True)
    caption = models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption 

class Comment(models.Model):
    comment = models.TextField(null=True)
    image_id = models.ForeignKey(Image,null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    likes = models.IntegerField(default=0, null=True)
    image_id = models.ForeignKey(Image,null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.likes