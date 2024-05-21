from django.shortcuts import render


# Models
from apps.posts.models import Post


def home_view(request):
    """HOME VIEW"""
    posts = Post.objects.all()

    return render(request, "posts/base.html", {"posts": posts})
