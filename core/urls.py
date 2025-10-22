from django.urls import path
from . import views
from django.views.generic import TemplateView
from core import views as core_views


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("ecommerce-demo/", core_views.mini_home, name="mini_home"),
    path(
        "digital-marketing-specialist",
        TemplateView.as_view(template_name="core/digital-marketing-specialist.html"),
        name="digital_marketing_specialist",
    ),
    path(
        "create-mini-ecommerce",
        TemplateView.as_view(template_name="core/create-mini-ecommerce.html"),
        name="mini_ecommerce",
    ),
    path(
        "ecommerce-site-builder",
        TemplateView.as_view(template_name="core/ecommerce-site-builder.html"),
        name="ecommerce_builder",
    ),
    path(
        "tech-va/",
        TemplateView.as_view(template_name="core/tech-va.html"),
        name="tech_va",
    ),
    path(
        "pdf-creation",
        TemplateView.as_view(template_name="core/pdf-creation.html"),
        name="pdf_creation",
    ),
    path("support/", views.support, name="support"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
