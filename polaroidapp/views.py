from email import message
from django.shortcuts import render, redirect
from .forms import RegisterForm, UploadForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment,Likes,User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method== 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm
    return render(request, 'registration/register_form.html', {'form':form})

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.session['_auth_user_id'])
    return render(request, 'profile.html', {'profile':profile})

@login_required
def results(request):
    if request.method == 'POST':
        if 'profiles' in request.POST and request.POST['profiles']:
            searched_profile = request.POST['profiles']
            profile_object = Profile.objects.filter(user__username__icontains=searched_profile)
            return render(request, 'search.html', {'profiles':profile_object})
        else:
            messages.error(request, "User does not exist!")
    return render(request, 'search.html')

@login_required
def feed(request):
    return render(request, 'feed.html') 