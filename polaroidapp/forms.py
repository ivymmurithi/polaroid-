from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['uploaded_image','image_name','caption']