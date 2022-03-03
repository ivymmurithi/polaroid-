from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.moethpd== 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = RegisterForm
    return render(request, 'registration/register_form.html', {'form':form})

def index(request):
    return render(request, 'index.html')