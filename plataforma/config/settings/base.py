# -*- coding: utf-8 -*-
"""Lo común a cualquier equipo.

**La base de datos de acá es un índice, no la fuente** (`DA-01`). La verdad vive
en archivos de texto dentro de `datos/`, y esta base se puede borrar entera y
reconstruir leyéndolos. Por eso el motor es un archivo local: no hay servicio
que levantar, y eso es lo que exigen `DA-03` y `RNF-08`.
"""
import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent

# Dónde vive lo que la plataforma guarda. Es la fuente: texto, versionable.
CARPETA_DATOS = RAIZ / "datos"

# Los validadores del estándar. La plataforma **lee** de ahí el enmascarador de
# claves, y nunca escribe. Copiarlo dejaría dos listas de secretos que se
# separan; moverlo obligaría a tocar el estándar sin comprar nada.
CARPETA_VALIDADORES = RAIZ.parent / "validadores"

# La clave solo firma las sesiones del navegador en esta máquina. Si no está
# puesta, se usa una de desarrollo: la plataforma no expone nada a la red.
SECRET_KEY = os.environ.get("CLAVE_DE_FIRMA", "clave-de-desarrollo-sin-valor")

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "nucleo.almacen",
    "nucleo.auditoria",
    "nucleo.proyectos",
]

# La plataforma corre en la máquina del usuario y no se expone a la red
# (`DA-03`), pero el formulario de conectar cambia estado, así que lleva su
# comprobación de origen igual: el día que corra en un servidor, ya está puesta.
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [RAIZ / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
    ]},
}]

WSGI_APPLICATION = "config.wsgi.application"

# El índice. Se borra y se rehace con `python manage.py reconstruir_indice`.
DATABASES = {"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": RAIZ / "indice.sqlite3",
}}

LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [RAIZ / "static"]
STATIC_ROOT = RAIZ / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
