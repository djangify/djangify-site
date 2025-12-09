from .models import Page


def published_pages(request):
    """Provide only published Pages to templates."""
    pages = Page.objects.filter(published=True).order_by("title")
    return {"published_pages": pages}
