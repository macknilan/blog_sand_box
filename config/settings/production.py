from .base import *  # noqa
from .base import env


# CORS NGINX
# TODO: ADD DOMAIN NAMES OF THE PRODUCTION SERVER

CSRF_TRUSTED_ORIGINS = ["https://mack.host"]

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")


# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["mack.host"])

# Django Admin URL.
ADMIN_URL = env("DJANGO_ADMIN_URL")
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("Rodolfo Ugalde", "nomackayu@gmail.com")]

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}

# The SECURE_PROXY_SSL_HEADER setting is a tuple representing a header/value pair
# that a reverse proxy (e.g., Nginx) sets when it receives secure traffic (HTTPS),
# which is then used by Django to determine whether a request is secure or not.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", defatult=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# TODO: CAMBIAR DESPUÉS A 5184000
SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", default="Mack")

SITE_NAME = "un bit perdido en el espacio"

SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Mack]")

# EMAIL
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = env("smtp.mailgun.org")
# EMAIL_HOST_USER = env("postmaster@mg.mack.host")
# EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DOMAIN = env("DOMAIN")

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    }
}

