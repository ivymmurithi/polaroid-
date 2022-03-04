from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment,Likes

# Create your views here.
def register(request):
    if request.method== 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = RegisterForm
    return render(request, 'registration/register_form.html', {'form':form})

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    profile_object = Profile.objects.all()
    return render(request, 'profile.html', {"profiles":profile_object})