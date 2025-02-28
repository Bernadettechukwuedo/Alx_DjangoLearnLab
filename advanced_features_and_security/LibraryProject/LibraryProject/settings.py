"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+nhj&uj1_tpu+mce#0w*!-crzkf-^3rj)=^%5)g$+9@c@@e$i!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
# Security Measures in This Django App

# 1. Cross-Site Scripting (XSS) Protection
# Enabled `SECURE_BROWSER_XSS_FILTER` to prevent XSS attacks.
# Implemented `Content Security Policy (CSP)` to restrict content sources.

# 2. Clickjacking Protection
# Set `X_FRAME_OPTIONS = "DENY"` to prevent embedding in iframes.

# 3. CSRF Protection
# Enabled CSRF middleware (`django.middleware.csrf.CsrfViewMiddleware`).
# All forms include `{% csrf_token %}`.

# 4. HTTPS Enforcement
# Configured `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`.
# Enabled `SECURE_SSL_REDIRECT = True` to force HTTPS.

# 5. Allowed Hosts and Headers
# Restricted `ALLOWED_HOSTS` to prevent host header attacks.
# Used `SECURE_CONTENT_TYPE_NOSNIFF` to prevent MIME sniffing attacks.

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",
]

MIDDLEWARE = [
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Content Security Policy Settings
CSP_DEFAULT_SRC = ("'self'",)  # Restrict content to your own domain
CSP_SCRIPT_SRC = (
    "'self'",
    "https://trusted-scripts.com",
)  # Allow scripts from trusted sources
CSP_STYLE_SRC = (
    "'self'",
    "https://trusted-styles.com",
    "'unsafe-inline'",
)  # Allow CSS sources
CSP_IMG_SRC = (
    "'self'",
    "https://trusted-images.com",
    "data:",
)  # Allow images from trusted sources
CSP_FONT_SRC = (
    "'self'",
    "https://fonts.gstatic.com",
)  # Allow fonts from Google Fonts or other sources
CSP_FRAME_ANCESTORS = (
    "'none'",
)  # Prevent embedding in iframes (clickjacking protection)
CSP_OBJECT_SRC = ("'none'",)  # Block Flash and other plugin content
CSP_MEDIA_SRC = ("'self'",)  # Restrict media sources
ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LibraryProject.wsgi.application"
AUTH_USER_MODEL = "bookshelf.CustomUser"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
