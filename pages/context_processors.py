from .models import Page


def published_pages(request):
    pages = Page.objects.filter(published=True, show_in_navigation=True).order_by(
        "menu_order", "title"
    )

    return {"published_pages": pages}
