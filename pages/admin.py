from django.contrib import admin
from .models import Page, PageSection, PageSettings, GalleryImage, HeroBanner, Hero


# Inline: Page sections inside a Page
class PageSectionInline(admin.StackedInline):
    model = PageSection
    extra = 0
    fields = (
        "section_type",
        "title",
        "subtitle",
        "body",
        "image",
        "order",
        "published",
    )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "template", "published", "menu_order")
    list_filter = ("template", "published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PageSectionInline]


@admin.register(PageSettings)
class PageSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "homepage_mode",
        "show_blog_on_homepage",
        "show_gallery_on_homepage",
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "published")
    list_editable = ("order", "published")


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ("text", "is_active")
    list_editable = ("is_active",)


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
