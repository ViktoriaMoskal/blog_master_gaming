from django.shortcuts import render
from django.http import HttpResponse


def post_lists(request):
    posts=[{'title': 'post1', 'body': 'body1'},{'title': 'post2', 'body': 'body2'},{'title': 'post3', 'body': 'body3'}]
    return render(request, 'blog/index.html', context={'posts': posts})

