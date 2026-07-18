from django.shortcuts import render

from .models import Gallery


def gallery(request):

    images = Gallery.objects.filter(
        is_active=True
    )

    return render(
        request,
        "gallery/gallery.html",
        {
            "images": images
        }
    )