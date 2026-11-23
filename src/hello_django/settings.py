from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-development-placeholder"
DEBUG = False
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "hello_django.urls"
MIDDLEWARE = []

INSTALLED_APPS = [
    "django.contrib.staticfiles"
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {}
    }
]

WSGI_APPLICATION = "hello_django.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]