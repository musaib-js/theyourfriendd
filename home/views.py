from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from accounts.models import Consultant
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()[0:3]
    consultant= Consultant.objects.all()[0:3]
    context = {'post':post, 'consultant':consultant}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def blogpost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    context = {'post':post}
    return render(request, 'blogpost.html', context)
