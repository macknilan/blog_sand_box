# Generated by Django 4.2.13 on 2024-06-07 18:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("posts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                db_column="author_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="author of the post",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="liked_posts",
                through="posts.LikedPost",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                to="posts.tag", verbose_name="tags for the post"
            ),
        ),
        migrations.AddField(
            model_name="likedpost",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="liked_post",
                to="posts.post",
                verbose_name="post liked",
            ),
        ),
        migrations.AddField(
            model_name="likedpost",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_liked_post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user who liked the post",
            ),
        ),
    ]
