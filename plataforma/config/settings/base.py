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
# Los moldes del estándar. Se leen cuando se piden: copiarlos los envejece.
CARPETA_PLANTILLAS = RAIZ.parent / "plantillas"

# La clave solo firma las sesiones del navegador en esta máquina. Si no está
# puesta, se usa una de desarrollo: la plataforma no expone nada a la red.
SECRET_KEY = os.environ.get("CLAVE_DE_FIRMA", "clave-de-desarrollo-sin-valor")

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    # `auth` trae las cuentas, los grupos y los permisos, con el cifrado de
    # contraseñas ya resuelto. **No se escribe uno propio**: autenticación
    # escrita a mano es la forma más común de escribirla mal (diseño §8.1).
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "nucleo.acceso",
    "nucleo.almacen",
    "nucleo.auditoria",
    "nucleo.proyectos",
    "nucleo.importacion",
    "nucleo.medicion",
    "nucleo.expediente",
    "nucleo.ciclo_de_vida",
    "nucleo.seguridad",
    "nucleo.comprobaciones",
    "nucleo.reglas",
    "nucleo.aprobaciones",
    "nucleo.memoria",
    "nucleo.avisos",
]

# La plataforma corre en la máquina del usuario y no se expone a la red
# (`DA-03`), pero el formulario de conectar cambia estado, así que lleva su
# comprobación de origen igual: el día que corra en un servidor, ya está puesta.
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # Pone en cada petición quién entró. Va después de la sesión porque la lee.
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Y esto exige haber entrado para todo lo que no esté en su lista corta.
    # Va acá y no como decorador por vista: una vista nueva nace protegida.
    "nucleo.acceso.middleware.ExigirHaberEntrado",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [RAIZ / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        # Para que la barra de arriba pueda decir quién entró.
        "django.contrib.auth.context_processors.auth",
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
# `terceros/` no se versiona: lo trae `descargar_estaticos.py`, pineado por
# versión y comprobado por huella. El estándar prohíbe copiar terceros al
# repositorio; se declaran y se instalan.
STATICFILES_DIRS = [RAIZ / "static", RAIZ / "terceros"]
STATIC_ROOT = RAIZ / "staticfiles"

# A dónde se manda a quien pide una pantalla sin haber entrado, y a dónde vuelve
# después. `LOGIN_REDIRECT_URL` casi nunca se usa: Django respeta a dónde iba.
LOGIN_URL = "entrar"
LOGIN_REDIRECT_URL = "proyectos-lista"
LOGOUT_REDIRECT_URL = "entrar"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
