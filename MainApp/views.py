from django.shortcuts import render
from django.views import generic

from blog.models import Post


# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'MainApp/home.html', {'posts': posts})


def about(request):
    return render(request, 'MainApp/about.html')
