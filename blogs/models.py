from django.db import models
from django.urls import reverse


class Blog(models.Model):

    title = models.CharField(max_length=250)

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to="blogs/",
        blank=True,
        null=True
    )

    short_description = models.CharField(
        max_length=300
    )

    content = models.TextField()

    author = models.CharField(
        max_length=100,
        default="Admin"
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["-created_at"]

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse(
            "blog_detail",
            kwargs={
                "slug": self.slug
            }
        )