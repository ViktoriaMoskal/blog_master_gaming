from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_lists(request):
    posts=Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
