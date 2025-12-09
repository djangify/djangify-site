from django.contrib import admin
from .models import Page, PageSection, PageSettings, HeroBanner


class PageSectionInline(admin.StackedInline):
    model = PageSection
    extra = 1
    ordering = ("order",)
    classes = ["collapse"]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "template", "published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PageSectionInline]


@admin.register(PageSettings)
class PageSettingsAdmin(admin.ModelAdmin):
    list_display = ("homepage_mode",)


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ("text", "is_active")
