from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
from django.conf import settings
from django.conf.urls.static import static


# Sitemap configuration
sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("core.urls")),

    path("blogs/", include("blogs.urls")),

    path("appointment/", include("appointments.urls")),

    path("contact/", include("contactus.urls")),

    path("gallery/", include("gallery.urls")),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )