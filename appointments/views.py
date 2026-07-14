from django.shortcuts import render, redirect
from .forms import AppointmentForm


def appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("appointment_success")

    else:

        form = AppointmentForm()

    return render(
        request,
        "appointments/appointment_form.html",
        {
            "form": form
        }
    )


def appointment_success(request):

    return render(
        request,
        "appointments/appointment_success.html"
    )