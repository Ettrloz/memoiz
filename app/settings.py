import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-bd)!ojzy4js9nsj_9wui(=7q1t)ctosx!c@gue0rtwgjf+_pk$"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "192.168.100.45"]

INSTALLED_APPS = [
    "authentication",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_vite_plugin",
    "core",
    "memoiz",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",)
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PGDATABASE"),
        "USER": os.getenv("PGUSER"),
        "PASSWORD": os.getenv("PGPASSWORD"),
        "HOST": os.getenv("PGHOST"),
        "PORT": "5432",
        "OPTIONS": {
            "sslmode": os.getenv("PGSSLMODE", "require"),
            "channel_binding": os.getenv("PGCHANNELBINDING", "prefer"),
        },
        "DISABLE_SERVER_SIDE_CURSORS": True,
        "CONN_HEALTH_CHECKS": True,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
]

AUTH_USER_MODEL = "authentication.User"

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "static"

DJANGO_VITE_PLUGIN = {
    "DEV_MODE": DEBUG,
    "BUILD_DIR": BASE_DIR / "static",
    "BUILD_URL_PREFIX": STATIC_URL,
    "SERVER": {"HOST": os.environ.get("DEV_HOST", "localhost"), "PORT": 9002, "PROTOCOL": "http"},
}

USE_I18N = True

LANGUAGE_CODE = "id"

LANGUAGES = [("id", "Bahasa Indonesia"), ("en", "English")]

LOCALE_PATHS = [BASE_DIR / "locale"]

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"
