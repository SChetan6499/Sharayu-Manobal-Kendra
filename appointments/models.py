from django.db import models


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    CONSULTATION_CHOICES = [
        ("Online", "Online"),
        ("Offline", "Offline"),
    ]

    name = models.CharField(max_length=150)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    consultation_type = models.CharField(
        max_length=20,
        choices=CONSULTATION_CHOICES
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    problem = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.appointment_date})"