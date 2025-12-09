from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class PageSettings(models.Model):
    HOMEPAGE_CHOICES = [
        ("SHOP", "Shop Homepage"),
        ("PAGES", "Pages Homepage"),
    ]
    homepage_mode = models.CharField(
        max_length=10, choices=HOMEPAGE_CHOICES, default="SHOP"
    )
    show_blog_on_homepage = models.BooleanField(
        default=False, help_text="Show the latest 3 blog posts on the homepage."
    )

    show_gallery_on_homepage = models.BooleanField(
        default=False, help_text="Show gallery images on the homepage."
    )

    def __str__(self):
        return "Pages Settings"


class Page(models.Model):
    TEMPLATE_CHOICES = [
        ("home", "Homepage"),
        ("about", "About"),
        ("custom", "Custom Page"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES)
    published = models.BooleanField(default=True)

    # SEO
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Navigation controls
    show_in_navigation = models.BooleanField(
        default=True, help_text="Show this page in the top navigation bar."
    )

    show_in_footer = models.BooleanField(
        default=True, help_text="Show this page in the footer links."
    )

    menu_order = models.PositiveIntegerField(
        default=0, help_text="Control the order of this page in the navigation."
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.template in ["home", "about"]:
            return reverse(f"pages:{self.template}")
        return reverse("pages:detail", args=[self.slug])


class PageSection(models.Model):
    SECTION_TYPES = [
        ("text", "Text Block"),
        ("two_column", "Two Column"),
        ("features", "Features Grid"),
        ("cta", "Call to Action"),
        ("faq", "FAQ List"),
        ("contact_form", "Contact Form"),
    ]

    page = models.ForeignKey(Page, related_name="sections", on_delete=models.CASCADE)
    section_type = models.CharField(max_length=50, choices=SECTION_TYPES)
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    body = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="pages/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page.title} – {self.section_type}"


class ThreeColumnBlock(models.Model):
    page = models.ForeignKey(
        Page, related_name="three_columns", on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    col_1_title = models.CharField(max_length=200, blank=True)
    col_1_body = HTMLField(blank=True, null=True)
    col_1_image = models.ImageField(upload_to="pages/columns/", blank=True, null=True)

    col_2_title = models.CharField(max_length=200, blank=True)
    col_2_body = HTMLField(blank=True, null=True)
    col_2_image = models.ImageField(upload_to="pages/columns/", blank=True, null=True)

    col_3_title = models.CharField(max_length=200, blank=True)
    col_3_body = HTMLField(blank=True, null=True)
    col_3_image = models.ImageField(upload_to="pages/columns/", blank=True, null=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"3-Column Block for {self.page.title}"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    title = models.CharField(max_length=200)
    caption = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title or f"Image {self.id}"


class HeroBanner(models.Model):
    text = models.CharField(max_length=200, default="New Resources Available!")
    action_text = models.CharField(max_length=100, default="See what's new")
    action_link = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    badge_text = models.CharField(max_length=50, default="New")

    class Meta:
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Banners"

    def __str__(self):
        return self.text


class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    body = HTMLField(blank=True, null=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=300, blank=True)

    image = models.ImageField(upload_to="hero/", blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.title
