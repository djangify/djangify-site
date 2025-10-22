from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("", include("infopages.urls")),
    path("news/", include("news.urls")),
    path("accounts/", include("accounts.urls")),
    path("shop/", include("shop.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("tinymce/", include("tinymce.urls")),
]

handler404 = "core.views.handler404"
handler500 = "core.views.handler500"
handler403 = "core.views.handler403"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
