from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'uploads/')
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    