"""MODEL POST FOR THE BLOG"""

import secrets
import string
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from nanoid import generate
from tinymce.models import HTMLField

# Utilities
from apps.utils.models import TimeStampedModel

# Models
from .tags import Tag


# https://docs.djangoproject.com/en/3.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
class PostLet(models.Manager):
    def get_queryset(self):
        """Show posts less than or equal to (lte) now"""
        now = timezone.now()
        return super().get_queryset().filter(publish_date__lte=now)


def unique_slugify(instance, string_to_slugify):
    """
    GENERATE A UNIQUE SLUG FOR A MODEL INSTANCE.
    """
    _slug = slugify(string_to_slugify)
    alphabet = "".join(
        secrets.choice(string.ascii_letters + string.digits + "-_") for i in range(31)
    )
    _slug_salt = f"{_slug}-{generate(alphabet, size=31)}"
    model = instance.__class__
    qs_exists = model.objects.filter(id=instance.id).exists()

    if qs_exists:
        return model.objects.filter(id=instance.id).values("url")[0]["url"]
    else:
        return _slug_salt


class Post(TimeStampedModel):
    """Post model."""

    id = models.UUIDField(
        _("id"),
        default=uuid.uuid4,
        db_column="post_id",
        editable=False,
        primary_key=True,
        unique=True,
    )
    title = models.CharField(_("title"), max_length=255)
    # body = models.TextField()
    body = HTMLField()
    image = models.ImageField(
        _("post_image"), upload_to="post_image/", max_length=500, blank=True, null=True
    )
    is_draft = models.BooleanField(_("is_draft"), default=False)
    publish_date = models.DateTimeField(
        _("published_date"), auto_now=False, auto_now_add=False, null=True, blank=True
    )
    url = models.SlugField(
        _("Url slug for link"), max_length=255, null=True, blank=True, unique=True
    )  # unique=True
    # link = models.URLField(_("link"), max_length=500, null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_("tags for the post"))
    objects = models.Manager()  # The default manager
    published = PostLet()  # The Post Manager manager
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_column="author_id",
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name=_("author of the post"),
    )  # SE HACE LA RELACIÓN POR QUE EN SETTINGS SE HACE LA RELACIÓN DE AUTH_USER_MODEL
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_posts", through="LikedPost"
    )

    class Meta(TimeStampedModel.Meta):
        """Overwrite meta class of TimeStampedModel"""

        # ordering = ("title",)
        ordering = ["-created_at"]
        db_table = "post_info"

    def __str__(self):
        """Return title and username."""
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        # self.url = slugify(self.title)
        name_to_slugify = self.title
        self.url = unique_slugify(self, name_to_slugify)
        super(Post, self).save(*args, **kwargs)
