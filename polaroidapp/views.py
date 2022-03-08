from django.shortcuts import render, redirect
from .forms import RegisterForm, UploadForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment,User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout

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
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['user_id'] = request.session['_auth_user_id']
            image = form.save()
            image.user_id = request.session['_auth_user_id']
            image.save()
            return redirect('/profile/',{'form':form})
        else:
            form = UploadForm()
    else:
        profile = Profile.objects.get(user=request.session['_auth_user_id'])
        image_objects = Image.objects.filter(user_id=request.session['_auth_user_id'])
        comments = Comment.objects.filter(image_id__user__id=profile.user.id)
        form = UploadForm()
        profile_form = ProfileForm()
    return render(request, 'profile.html', {'profile':profile,'images':image_objects, 'comments': comments, 'form':form, 'profileform':profile_form})

@login_required
def uploadprofile(request):
    if request.method == 'POST':
        user = Profile.objects.get(user_id=request.session['_auth_user_id'])
        profile_form = ProfileForm(request.POST, request.FILES,instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/profile/',{'form':profile_form})
        else:
            profile_form = ProfileForm()
    else:
        profile_form = ProfileForm()
    return render(request, 'profile.html', {'profileform':profile_form})

@login_required
def results(request):
    if request.method == 'POST':
        if 'profiles' in request.POST and request.POST['profiles']:
            searched_profile = request.POST['profiles']
            profile_object = Profile.objects.filter(user__username__icontains=searched_profile)
            profile_ids = [profile.user.id for profile in profile_object]
            uploads_object = Image.objects.filter(user_id__in=profile_ids)
            return render(request, 'search.html', {'profiles':profile_object,'images':uploads_object})
        else:
            messages.error(request, "User does not exist!")
    return render(request, 'search.html')

@login_required
def likes(request):
    image_id = request.POST.get("image_id")
    image = Image.objects.get(pk=image_id)
    like_count = image.likes + 1
    Image.objects.filter(pk=image_id).update(likes=like_count)

    return JsonResponse({"liked": True, "likes": like_count})

@login_required
def comment(request):
    image_id = request.POST.get("image_id")
    image = Image.objects.get(pk=image_id)
    comment_value = request.POST.get("comment_value")
    user_id = request.session['_auth_user_id']
    user = User.objects.get(pk=user_id)
    comment = Comment.objects.create(
        comment= comment_value,
        user = user,
        image_id=image
    )
    return JsonResponse({'comment':comment.comment, 'user':user.username})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')