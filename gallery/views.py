from django.shortcuts import render
from .models import Gallery


def gallery(request):

    category = request.GET.get("category")

    if category:
        images = Gallery.objects.filter(
            category=category,
            is_active=True
        )
    else:
        images = Gallery.objects.filter(
            is_active=True
        )

    categories = Gallery.objects.values_list(
        "category",
        flat=True
    ).distinct()

    context = {
        "images": images,
        "categories": categories,
        "selected_category": category,
    }

    return render(
        request,
        "gallery/gallery.html",
        context
    )