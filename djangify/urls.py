from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

from .sitemaps import sitemaps
from pages.views import home_view


def dynamic_home(request):
    return home_view(request)


urlpatterns = [
    path("admin/", admin.site.urls),
    # ---- ROOT HOMEPAGE LOGIC FIRST ----
    path("", dynamic_home, name="home"),
    # ---- PAGE-BASED ROUTES ----
    path("pages/", include("pages.urls", namespace="pages")),
    path("", include("infopages.urls")),  # this is okay because it uses specific slugs
    # ---- NEWS / BLOG ----
    path("news/", include("news.urls")),
    # ---- ACCOUNTS ----
    path("accounts/", include("accounts.urls")),
    # ---- SHOP ----
    path("shop/", include("shop.urls")),
    # ---- CORE (STATIC SITE PAGES LIKE ABOUT ETC) ----
    # IMPORTANT: core.urls should NOT take over the root path anymore.
    # Only include it under a namespace prefix if needed.
    path("core/", include("core.urls", namespace="core")),
    # ---- SITEMAP ----
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # ---- TINYMCE ----
    path("tinymce/", include("tinymce.urls")),
]

# ---- ERROR HANDLERS ----
handler404 = "core.views.handler404"
handler500 = "core.views.handler500"
handler403 = "core.views.handler403"

# ---- STATIC/MEDIA ----
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
