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

    def __str__(self):
        return "Pages Settings"


class Page(models.Model):
    TEMPLATE_CHOICES = [
        ("home", "Homepage"),
        ("about", "About"),
        ("services", "Services"),
        ("contact", "Contact"),
        ("custom", "Custom Page"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES)
    published = models.BooleanField(default=True)

    # Content blocks
    content_block_1 = HTMLField(blank=True, null=True)
    content_block_2 = HTMLField(blank=True, null=True)
    content_block_3 = HTMLField(blank=True, null=True)

    # SEO
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.template in ["home", "about", "services", "contact"]:
            return reverse(f"pages:{self.template}")
        return reverse("pages:detail", args=[self.slug])


class PageSection(models.Model):
    SECTION_TYPES = [
        ("hero", "Hero"),
        ("text", "Text Block"),
        ("two_column", "Two Column"),
        ("features", "Features Grid"),
        ("cta", "Call to Action"),
        ("faq", "FAQ List"),
        ("image_full", "Full Width Image"),
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
