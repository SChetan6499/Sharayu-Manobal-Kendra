from django.shortcuts import render
from services.models import Service
from testimonials.models import Testimonial


def home(request):

    services = Service.objects.filter(
        is_active=True
    )

    testimonials = Testimonial.objects.filter(
        is_active=True
    )

    context = {

        "services": services,
        "testimonials": testimonials,

    }

    return render(
        request,
        "core/home.html",
        context
    )