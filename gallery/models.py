from django.db import models


class Gallery(models.Model):

    CATEGORY_CHOICES = [

        ("Clinic", "Clinic"),

        ("Counselling", "Counselling"),

        ("Workshop", "Workshop"),

        ("Events", "Events"),

        ("Other", "Other"),

    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Clinic"
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    description = models.TextField(
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            "display_order",
            "-created_at"
        ]

    def __str__(self):

        return self.title