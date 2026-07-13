from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "rating",
        "display_order",
        "is_active",
    )

    list_filter = (
        "rating",
        "is_active",
    )

    search_fields = (
        "name",
        "designation",
    )

    ordering = (
        "display_order",
    )