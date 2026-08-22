# -*- coding: utf-8 -*-
"""Lo común a cualquier equipo. Lo del equipo de desarrollo vive en local.py.

Las credenciales no viven en el código: se leen de variables de entorno, y en
desarrollo las carga el .env (interfaz/.env, que no se versiona; la lista de
variables, sin valores, está en interfaz/.env.example).
"""
import io
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def _cargar_env(ruta):
    """Carga un .env plano al entorno, sin pisar lo ya definido."""
    if not ruta.is_file():
        return
    for linea in io.open(ruta, encoding="utf-8"):
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        os.environ.setdefault(clave.strip(), valor.strip())


_cargar_env(BASE_DIR / ".env")

SECRET_KEY = os.environ.get("SECRET_KEY", "")
DEBUG = False
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'cimiento.visor',
    'cimiento.proyectos',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
        'cimiento.visor.core.nav',
    ]},
}]

WSGI_APPLICATION = 'config.wsgi.application'

# Base propia de Django (no se usa para la memoria; esa es senales.db aparte).
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': BASE_DIR / '_visor.sqlite3'}}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# static/ es solo lo propio; terceros/ lo llena descargar_estaticos.py y no se versiona.
STATICFILES_DIRS = [BASE_DIR / 'static', BASE_DIR / 'terceros']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
USE_TZ = True
