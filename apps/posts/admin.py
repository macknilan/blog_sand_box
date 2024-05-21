"""POST MODELS ADMIN."""

from django.contrib import admin

# Models
from apps.posts.models import (
    Post,
    Tag,
    LikedPost
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """PROFILE MODEL ADMIN"""

    list_display = [
        "id",
        "title",
        "body",
        "image",
        "is_draft",
        "url",
        "publish_date",
    ]
    search_fields = [
        "title",
        "publish_date",
    ]
    list_filter = [
        "is_draft",
        "publish_date",
    ]
    list_display_links = [
        "id",
        "title",
    ]
    list_editable = [
        "is_draft",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """TAG MODEL ADMIN"""

    list_display = [
        "id",
        "name",
        "slug",
        "image",
    ]
    search_fields = [
        "name",
    ]
    list_display_links = [
        "id",
        "name",
    ]
    list_editable = [
        "slug",
    ]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (
            "Tag",
            {
                "fields": (
                    "name",
                    "slug",
                    "image",
                )
            },
        ),
    )
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at"
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]


@admin.register(LikedPost)
class LikedPostAdmin(admin.ModelAdmin):
    """
    LIKED POST MODEL ADMIN
    """
    list_display = [
        "id",
        "user",
        "post",
    ]
    search_fields = [
        "user",
        "post",
    ]
    list_display_links = [
        "id",
        "user",
    ]
    list_editable = [
        "post",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            "Liked Post",
            {
                "fields": (
                    "user",
                    "post",
                )
            },
        ),
    )
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at"
    ]
