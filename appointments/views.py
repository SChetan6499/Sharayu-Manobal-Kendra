from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import AppointmentForm


def appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save()

            try:

                # ==========================================
                # Email to Patient
                # ==========================================

                send_mail(
                    subject="Appointment Confirmation - Sharayu Manobal Kendra",

                    message=f"""
Dear {appointment.name},

Thank you for booking your appointment with Sharayu Manobal Kendra.

Your appointment has been received successfully.

Appointment Details
----------------------------

Date : {appointment.appointment_date}

Time : {appointment.appointment_time}

Consultation : {appointment.consultation_type}

Our counsellor will contact you shortly to confirm your appointment.

Thank you for choosing us.

Regards,

Sharayu Manobal Kendra
""",

                    from_email=settings.DEFAULT_FROM_EMAIL,

                    recipient_list=[appointment.email],

                    fail_silently=False,
                )

                # ==========================================
                # Email to Counsellor / Admin
                # ==========================================

                send_mail(
                    subject="🔔 New Appointment Booking",

                    message=f"""
A new appointment has been booked.

----------------------------------------

Patient Name : {appointment.name}

Age : {appointment.age}

Gender : {appointment.gender}

Phone : {appointment.phone}

Email : {appointment.email}

Consultation : {appointment.consultation_type}

Appointment Date : {appointment.appointment_date}

Appointment Time : {appointment.appointment_time}

----------------------------------------

Problem Description

{appointment.problem}

----------------------------------------

Please log in to the Django Admin panel to review and manage this appointment.
""",

                    from_email=settings.DEFAULT_FROM_EMAIL,

                    # Change this later to your clinic email if needed
                    recipient_list=[settings.EMAIL_HOST_USER],

                    fail_silently=False,
                )

            except Exception as e:

                print("Email Error:", e)

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