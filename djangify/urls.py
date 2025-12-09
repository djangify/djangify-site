from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
from django.conf import settings
from django.conf.urls.static import static
from pages.models import PageSettings


def dynamic_home(request):
    settings = PageSettings.objects.first()
    if settings and settings.homepage_mode == "PAGES":
        from pages.views import home_view

        return home_view(request)
    from shop.views import product_list

    return product_list(request)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("", dynamic_home, name="home"),
    path("", include("pages.urls")),
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
