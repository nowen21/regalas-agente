# -*- coding: utf-8 -*-
"""Lo común a cualquier equipo.

Sigue `plantillas/estructura-proyecto-django.md` del estándar: lo de cada equipo
va en su propio archivo (`local.py`), y lo de cada máquina en el `.env`, que no
se versiona (`00·N6`).
"""
import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent

# La clave solo firma las sesiones del navegador. Sin `.env`, se usa una de
# desarrollo: sirve para trabajar en esta máquina y nada más.
SECRET_KEY = os.environ.get("CLAVE_DE_FIRMA", "clave-de-desarrollo-sin-valor")

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Las de Django primero; los módulos de `core/` se agregan después, cada uno con
# su `apps.py`, en orden de dependencia (catálogos primero).
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [RAIZ / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Un archivo local: no hay motor que levantar aparte.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": RAIZ / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [RAIZ / "static"]       # solo lo propio del proyecto
STATIC_ROOT = RAIZ / "staticfiles"         # lo junta `collectstatic`; no se versiona

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
