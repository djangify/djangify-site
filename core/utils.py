# core/utils.py
from django.urls import reverse


def get_home_url():
    try:
        from pages.models import PageSettings

        settings = PageSettings.objects.first()
    except Exception:
        settings = None

    if settings and settings.homepage_mode == "PAGES":
        return reverse("pages:home")

    # Fallback to shop if available
    try:
        return reverse("shop:product_list")
    except Exception:
        return "/"
