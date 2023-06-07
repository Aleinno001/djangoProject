from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Category
from .forms import CommentForm, PostForm


# Create your views here.

def detail(request, category_slug, slug):
    if request.user.is_authenticated is False:
        post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    else:
        post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            form = CommentForm()
    else:
        if request.method == 'POST' and request.user.is_authenticated is False:
            return redirect('loginPage')

    form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | Q(body__icontains=query) | Q(intro__icontains=query))
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})


@login_required(login_url='loginPage')
def managePost(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/managePost.html', {'posts': posts})


def savePost(request, postid):
    pass


# post = Post.objects.get(pk=id)
# you can do this for as many fields as you like
# here I asume you had a form with input like <input type="text" name="name"/>
# so it's basically like that for all form fields
# emp.name = request.POST.get('name')
# emp.save()
# return HttpResponse('updated')


def delete(request, postid):
    post = Post.objects.get(pk=postid)
    post.delete()
    return redirect('managePost')


def createPost(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = Post.ACTIVE
            post.slug = post.title.replace(' ', '-')
            post.save()
            return redirect('managePost')

        else:
            return redirect('managePost')
    else:
        if request.method == 'POST' and request.user.is_authenticated is False:
            return redirect('loginPage')

    form = PostForm()

    return render(request, 'blog/createPost.html', {'form': form})
