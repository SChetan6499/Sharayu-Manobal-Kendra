from django.db import models


class Testimonial(models.Model):

    name = models.CharField(max_length=150)

    designation = models.CharField(
        max_length=200,
        blank=True
    )

    photo = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    review = models.TextField()

    rating = models.PositiveSmallIntegerField(
        default=5
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name