from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import (
    Page,
    PageSection,
    ThreeColumnBlock,
    PageSettings,
    GalleryImage,
    HeroBanner,
    Hero,
)


# Make HTML optional
class PageSectionForm(forms.ModelForm):
    class Meta:
        model = PageSection
        fields = "__all__"

    body = forms.CharField(widget=TinyMCE(), required=False)


class PageSectionInline(admin.StackedInline):
    model = PageSection
    form = PageSectionForm
    extra = 1
    can_delete = True

    fieldsets = (
        (
            "Page Section",
            {
                "fields": (
                    "section_type",
                    "title",
                    "subtitle",
                    "body",
                    "image",
                    "button_text",
                    "button_link",
                    "order",
                    "published",
                )
            },
        ),
    )


class ThreeColumnInline(admin.StackedInline):
    model = ThreeColumnBlock
    extra = 0
    can_delete = True

    fieldsets = (
        (
            "3-Column Block",
            {
                "classes": ("collapse",),
                "fields": (
                    "published",
                    "order",
                    ("col_1_title", "col_1_image"),
                    "col_1_body",
                    ("col_2_title", "col_2_image"),
                    "col_2_body",
                    ("col_3_title", "col_3_image"),
                    "col_3_body",
                ),
            },
        ),
    )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "template", "published", "menu_order")
    list_filter = ("template", "published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PageSectionInline, ThreeColumnInline]


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
