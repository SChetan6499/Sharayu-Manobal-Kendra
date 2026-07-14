from django.shortcuts import render

from services.models import Service

from testimonials.models import Testimonial

from blogs.models import Blog


def home(request):

    services = Service.objects.filter(
        is_active=True
    )

    testimonials = Testimonial.objects.filter(
        is_active=True
    )

    latest_blogs = Blog.objects.filter(
        is_published=True
    )[:3]

    context = {

        "services": services,

        "testimonials": testimonials,

        "latest_blogs": latest_blogs,

    }

    return render(
        request,
        "core/home.html",
        context
    )