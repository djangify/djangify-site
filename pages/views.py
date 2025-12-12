from django.shortcuts import render, get_object_or_404
from .models import Page, PageSettings, HeroBanner, GalleryImage, Hero
from django.http import Http404
from news.models import Post


def _render_page(request, template_name):
    page = get_object_or_404(Page, template=template_name, published=True)
    sections = page.sections.filter(published=True)
    return render(
        request, f"pages/{template_name}.html", {"page": page, "sections": sections}
    )


def home_view(request):
    settings_obj = PageSettings.objects.first()
    if not settings_obj:
        raise Http404("Page settings missing")

    # Shop homepage shortcut
    if settings_obj.homepage_mode == "SHOP":
        return render(request, "shop/home.html", {})

    page = get_object_or_404(Page, template="home", published=True)

    # Core page blocks
    sections = list(page.sections.filter(published=True))
    three_columns = list(page.three_columns.filter(published=True))
    galleries = list(page.galleries.filter(published=True))

    content_blocks = sorted(
        sections + three_columns + galleries,
        key=lambda block: block.order,
    )

    # Homepage-only blog feature
    blog_posts = None
    if settings_obj.show_blog_on_homepage:
        blog_posts = Post.objects.filter(status="published").order_by("-publish_date")[
            :3
        ]

    context = {
        "page": page,
        "content_blocks": content_blocks,
        "hero": Hero.objects.filter(is_active=True).first(),
        "hero_banner": HeroBanner.objects.filter(is_active=True).first(),
        "blog_posts": blog_posts,
    }

    return render(request, "pages/home.html", context)


def gallery_view(request):
    page = get_object_or_404(Page, template="gallery", published=True)

    sections = list(page.sections.filter(published=True))
    three_columns = list(page.three_columns.filter(published=True))
    galleries = list(page.galleries.filter(published=True))

    content_blocks = sorted(
        sections + three_columns + galleries,
        key=lambda block: block.order,
    )

    context = {
        "page": page,
        "content_blocks": content_blocks,
    }

    return render(request, "pages/gallery.html", context)


def about_view(request):
    page = get_object_or_404(Page, template="about", published=True)

    sections = list(page.sections.filter(published=True))
    three_columns = list(page.three_columns.filter(published=True))
    galleries = list(page.galleries.filter(published=True))

    content_blocks = sorted(
        sections + three_columns + galleries,
        key=lambda block: block.order,
    )

    context = {
        "page": page,
        "content_blocks": content_blocks,
    }

    return render(request, "pages/about.html", context)


def detail_view(request, slug):
    page = get_object_or_404(Page, slug=slug, published=True)

    sections = list(page.sections.filter(published=True))
    three_columns = list(page.three_columns.filter(published=True))
    galleries = list(page.galleries.filter(published=True))

    content_blocks = sorted(
        sections + three_columns + galleries,
        key=lambda block: block.order,
    )

    context = {
        "page": page,
        "content_blocks": content_blocks,
    }

    return render(request, "pages/custom.html", context)


def gallery_image_modal(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk, published=True)

    gallery = image.gallery
    images = list(gallery.images.filter(published=True).order_by("order", "id"))

    index = images.index(image)

    prev_image = images[index - 1] if index > 0 else None
    next_image = images[index + 1] if index < len(images) - 1 else None

    context = {
        "image": image,
        "prev_image": prev_image,
        "next_image": next_image,
    }

    return render(request, "gallery/modal.html", context)
