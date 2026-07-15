from django.db import models


class Service(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True, null=True)

    icon = models.CharField(max_length=100)

    short_description = models.CharField(max_length=300)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title