from django.shortcuts import get_object_or_404, render

# Models
from apps.posts.models import Post


def home_view(request):
    """HOME VIEW"""
    posts = Post.objects.all().values("id", "title", "url", "created_at")

    return render(request, "posts/base.html", {"posts": posts})


def post_detail_view(request, url):
    """
    POST DETAIL VIEW
    """
    post = get_object_or_404(Post, url=url)

    context = {"post": post}

    return render(request, "posts/post_detail.html", context)
