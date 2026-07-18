from django.db import models


class Contact(models.Model):

    STATUS_CHOICES = [
        ("New", "New"),
        ("Replied", "Replied"),
        ("Closed", "Closed"),
    ]

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="New"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name