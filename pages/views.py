from django.shortcuts import render, get_object_or_404
from .models import Page, PageSettings, HeroBanner


def _render_page(request, template_name):
    page = get_object_or_404(Page, template=template_name, published=True)
    sections = page.sections.filter(published=True)
    return render(
        request, f"pages/{template_name}.html", {"page": page, "sections": sections}
    )


def home_view(request):
    # Get homepage settings (optional)
    settings_obj = PageSettings.objects.first()

    # Get the homepage page object
    page = get_object_or_404(Page, template="home", published=True)

    # Get published sections (ordered)
    sections = page.sections.filter(published=True).order_by("order")

    # Active hero banner (optional)
    banner = HeroBanner.objects.filter(is_active=True).first()

    context = {
        "page": page,
        "sections": sections,
        "banner": banner,
    }

    return render(request, "pages/home.html", context)


def about_view(request):
    page = get_object_or_404(Page, template="about", published=True)
    sections = page.sections.filter(published=True).order_by("order")

    context = {
        "page": page,
        "sections": sections,
    }

    return render(request, "pages/about.html", context)


def services_view(request):
    page = get_object_or_404(Page, template="services", published=True)
    sections = page.sections.filter(published=True).order_by("order")

    context = {
        "page": page,
        "sections": sections,
    }

    return render(request, "pages/services.html", context)


def contact_view(request):
    page = get_object_or_404(Page, template="contact", published=True)
    sections = page.sections.filter(published=True).order_by("order")

    context = {
        "page": page,
        "sections": sections,
    }

    return render(request, "pages/contact.html", context)


def detail_view(request, slug):
    page = get_object_or_404(Page, slug=slug, published=True)
    sections = page.sections.filter(published=True).order_by("order")

    context = {
        "page": page,
        "sections": sections,
    }

    return render(request, "pages/custom.html", context)
