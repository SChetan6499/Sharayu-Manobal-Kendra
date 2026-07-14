from django.contrib import admin
from django.utils.html import format_html
from .models import Appointment


@admin.action(description="Mark selected appointments as Confirmed")
def mark_confirmed(modeladmin, request, queryset):
    queryset.update(status="Confirmed")


@admin.action(description="Mark selected appointments as Completed")
def mark_completed(modeladmin, request, queryset):
    queryset.update(status="Completed")


@admin.action(description="Mark selected appointments as Cancelled")
def mark_cancelled(modeladmin, request, queryset):
    queryset.update(status="Cancelled")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "appointment_date",
        "appointment_time",
        "consultation_type",
        "colored_status",
    )

    list_filter = (
        "status",
        "consultation_type",
        "appointment_date",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-appointment_date",
        "-appointment_time",
    )

    actions = [
        mark_confirmed,
        mark_completed,
        mark_cancelled,
    ]

    fieldsets = (

        ("Patient Information", {
            "fields": (
                "name",
                "age",
                "gender",
                "phone",
                "email",
            )
        }),

        ("Appointment Details", {
            "fields": (
                "consultation_type",
                "appointment_date",
                "appointment_time",
                "problem",
            )
        }),

        ("Status", {
            "fields": (
                "status",
                "created_at",
            )
        }),
    )

    def colored_status(self, obj):

        colors = {
            "Pending": "orange",
            "Confirmed": "blue",
            "Completed": "green",
            "Cancelled": "red",
        }

        color = colors.get(obj.status, "black")

        return format_html(
            '<strong style="color:{};">{}</strong>',
            color,
            obj.status,
        )

    colored_status.short_description = "Status"