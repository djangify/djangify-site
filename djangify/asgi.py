import os

from django.core.asgi import get_asgi_application

# Set the default settings module for production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangify.settings.production")

application = get_asgi_application()
