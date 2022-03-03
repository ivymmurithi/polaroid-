from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'registration/register_form.html')

def index(request):
    return render(request, 'index.html')