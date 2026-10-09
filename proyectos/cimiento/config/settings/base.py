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
    "core.inicio",
    "core.cuentas",
    "core.proyectos",
    "core.niveles",
    "core.consumo",
    "core.ayuda",
    "core.historia",
    "core.estandar",
    "core.pruebas",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # La base se revisa antes que la entrada: revisar la sesión ya la usa, y
    # su error saldría como una página 500 en vez de decir qué hacer.
    "core.inicio.middleware.BaseApagada",
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
    # `EP-026·HU-001` · Lo que se guarda en la petición queda a nombre de su cuenta.
    "core.historia.middleware.CuentaDeLaPeticion",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Toda pantalla pide entrar (`LoginRequiredMiddleware`); estas son las rutas.
LOGIN_URL = "cuentas:entrar"
LOGIN_REDIRECT_URL = "inicio:inicio"
LOGOUT_REDIRECT_URL = "cuentas:entrar"

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
                "core.inicio.pendientes.pendientes",
            ],
        },
    },
]

# MariaDB, con la conexión del `.env` (`00·N6`). Django usa para ella el mismo
# motor que para MySQL. `manage.py preparar_base` la crea si falta y la migra.
# Con `or` y no con el valor por defecto de `get`: una variable copiada de
# `.env.example` sin llenar llega vacía, y vacía no es un nombre de base.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NOMBRE") or "cimiento",
        "USER": os.environ.get("DB_USUARIO") or "root",
        "PASSWORD": os.environ.get("DB_CLAVE", ""),
        "HOST": os.environ.get("DB_SERVIDOR") or "127.0.0.1",
        "PORT": os.environ.get("DB_PUERTO") or "3307",
        # InnoDB a la fuerza: el MariaDB de WAMP crea las tablas con MyISAM,
        # que no tiene transacciones ni llaves foráneas.
        "OPTIONS": {"charset": "utf8mb4",
                    "init_command": "SET default_storage_engine=INNODB"},
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
# Lo propio del proyecto, y de lo que instala npm solo la carpeta `dist` de
# cada paquete: Django no ve el resto de `node_modules/` (`10·DEP2`).
# Sin prefijo: en Windows, Django 5.2 compara el prefijo con `\` y la URL llega
# con `/`, así que una carpeta con prefijo nunca se sirve.
NPM = RAIZ / "node_modules"
STATICFILES_DIRS = [
    RAIZ / "static",
    # `EP-028·HU-007` · La plantilla de Cimiento es AdminLTE 4, sobre Bootstrap 5.
    NPM / "admin-lte" / "dist",            # css/adminlte.min.css, js/adminlte.min.js
    NPM / "bootstrap" / "dist",            # js/bootstrap.bundle.min.js
    NPM / "bootstrap-icons" / "font",      # bootstrap-icons.min.css y fonts/
    NPM / "list.js" / "dist",              # list.js: ordenar, filtrar y paginar las tablas
    NPM / "htmx.org" / "dist",             # htmx.min.js
    NPM / "apexcharts" / "dist",           # apexcharts.min.js
]
STATIC_ROOT = RAIZ / "staticfiles"         # lo junta `collectstatic`; no se versiona

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
