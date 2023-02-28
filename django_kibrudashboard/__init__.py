import django

version = "1.0.1"

if django.VERSION < (3, 2):
    default_app_config = "django_kibrudashboard.apps.KibruConfig"
