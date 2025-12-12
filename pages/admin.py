from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import (
    Page,
    PageSection,
    ThreeColumnBlock,
    PageSettings,
    GalleryImage,
    GalleryBlock,
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


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    ordering = ("order",)


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


class GalleryBlockInline(admin.StackedInline):
    model = GalleryBlock
    extra = 0
    can_delete = True
    ordering = ("order",)
    fields = ("title", "order", "published")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "template", "published", "menu_order")
    list_filter = ("template", "published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        PageSectionInline,
        ThreeColumnInline,
        GalleryBlockInline,
    ]


@admin.register(PageSettings)
class PageSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "homepage_mode",
        "show_blog_on_homepage",
        "show_gallery_on_homepage",
    )


@admin.register(GalleryBlock)
class GalleryBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "order", "published")
    list_filter = ("page", "published")
    ordering = ("page", "order")
    readonly_fields = ("page",)

    inlines = [GalleryImageInline]

    def has_add_permission(self, request):
        return False  # removes the button that allows to add a gallery


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ("text", "is_active")
    list_editable = ("is_active",)


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
