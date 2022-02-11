from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost

# Create your views here.


def index(request):
    posts = blogPost.objects.all()
    print(posts)
    return render(request, "blog/index.html", {'posts': posts})


def blogpost(request, id):
    post = blogPost.objects.filter(post_id=id)[0]
    return render(request, "blog/blogpost.html", {'post': post})
