from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        """
        Save profile objects
        """
        self.save()

    def delete_profile(self):
        """
        Delete profile objects
        """
        self.delete()

class Image(models.Model):
    uploaded_image = models.ImageField(upload_to = 'uploads/', null=True)
    image_name = models.CharField(max_length=30, null=True)
    caption = models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.image_name

    def save_image(self):
        """
        Save image objects
        """
        self.save()

    def delete_image(self):
        """
        Delete image objects
        """
        self.delete() 

class Comment(models.Model):
    comment = models.TextField(null=True)
    image_id = models.ForeignKey(Image,null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def save_comment(self):
        """
        Save comment objects
        """
        self.save()

    def delete_comment(self):
        """
        Delete comment objects
        """
        self.delete()