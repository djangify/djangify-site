from django.shortcuts import render, get_object_or_404
from .models import Page, PageSettings, HeroBanner, GalleryImage, Hero, ThreeColumnBlock
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

    # Determine which homepage to show
    if settings_obj.homepage_mode == "SHOP":
        return render(request, "shop/home.html", {})

    # Load the actual "home" page
    try:
        page = Page.objects.get(template="home", published=True)
    except Page.DoesNotExist:
        raise Http404("Homepage does not exist")

    # All published sections for the homepage
    sections = page.sections.filter(published=True).order_by("order")
    three_columns = ThreeColumnBlock.objects.filter(page=page, published=True).order_by(
        "order"
    )

    # Hero banner (optional)
    hero_banner = HeroBanner.objects.filter(is_active=True).first()
    hero = Hero.objects.filter(is_active=True).first()

    # Blog posts
    blog_posts = None
    if settings_obj.show_blog_on_homepage:
        blog_posts = Post.objects.filter(status="published").order_by("-created")[:3]

    # Gallery
    gallery_items = None
    if settings_obj.show_gallery_on_homepage:
        gallery_items = GalleryImage.objects.filter(published=True).order_by("order")[
            :6
        ]

    context = {
        "page": page,
        "sections": sections,
        "hero": hero,
        "hero_banner": hero_banner,
        "three_columns": three_columns,
        "blog_posts": blog_posts,
        "gallery_items": gallery_items,
    }

    return render(request, "pages/home.html", context)


def about_view(request):
    page = get_object_or_404(Page, template="about", published=True)
    sections = page.sections.filter(published=True).order_by("order")
    three_columns = ThreeColumnBlock.objects.filter(page=page, published=True).order_by(
        "order"
    )
    context = {
        "page": page,
        "sections": sections,
        "three_columns": three_columns,
    }

    return render(request, "pages/about.html", context)


def detail_view(request, slug):
    page = get_object_or_404(Page, slug=slug, published=True)
    sections = page.sections.filter(published=True).order_by("order")
    three_columns = ThreeColumnBlock.objects.filter(page=page, published=True).order_by(
        "order"
    )
    context = {
        "page": page,
        "sections": sections,
        "three_columns": three_columns,
    }

    return render(request, "pages/custom.html", context)


def gallery_image_modal(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    return render(request, "gallery/modal.html", {"image": image})
