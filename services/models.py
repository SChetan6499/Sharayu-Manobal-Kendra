from django.db import models


class Service(models.Model):

    title = models.CharField(max_length=200)

    icon = models.CharField(
        max_length=50,
        help_text="Font Awesome icon class (Example: fa-solid fa-brain)"
    )

    short_description = models.TextField()

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["display_order", "title"]

        verbose_name = "Service"

        verbose_name_plural = "Services"

    def __str__(self):
        return self.title