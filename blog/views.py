from django.shortcuts import render
from . models import * 

# Create your views here.
def index(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'authors' : authors,
        'categories' : categories,
        'posts' : posts
    })

def display_categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {
        'categories' : categories
    })

def display_authors(request):
    authors = Author.objects.all()
    return render(request, 'blog/index.html', {
        'authors' : authors
    })

def display_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'posts' : posts
    })