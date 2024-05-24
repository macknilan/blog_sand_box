from django.urls import path

from apps.posts.views import post_detail_view

app_name = "posts"

urlpatterns = [
    path("detail/<pk>/", post_detail_view, name="post-detail"),
]
