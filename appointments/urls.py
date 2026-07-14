from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.appointment,
        name="appointment"
    ),

    path(
        "success/",
        views.appointment_success,
        name="appointment_success"
    ),

]