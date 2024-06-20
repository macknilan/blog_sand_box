from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

# Models
from apps.users.models import Profile, User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """USER MODEL ADMIN."""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("username", "first_name", "last_name", "phone_number")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_verified",
                    "is_client",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["id", "username"]
    search_fields = ["username", "email"]


@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    """Profile model admin"""

    def username(self, obj):
        return obj.user.username

    username.short_description = "Username"

    list_display = [
        "username",
        "biography",
        "picture",
        "created_at",
        "updated_at",
    ]

    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    fieldsets = [
        (
            _("Profile"),
            {
                "fields": (("user", "biography", "picture"),),
            },
        ),
    ]
