"""POST MODELS ADMIN."""

from django.contrib import admin

# Models
from apps.posts.models import LikedPost, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """PROFILE MODEL ADMIN"""

    list_display = [
        "id",
        "title",
        "short_body",
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

    def short_body(self, obj):
        """RETURN THE FIRST 50 WORDS OF THE BODY FIELD."""
        words = obj.body.split()[:15]
        return ' '.join(words) + '...' if len(words) > 15 else ' '.join(words)


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
