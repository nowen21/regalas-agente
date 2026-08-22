# -*- coding: utf-8 -*-
"""Lo del equipo de desarrollo: el visor corriendo en la máquina local."""
from .base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ['*']

# El visor es una herramienta local sin datos de terceros; esta llave de
# desarrollo no protege nada y no viaja a ningún despliegue (ahí manda base.py,
# que la exige por variable de entorno).
SECRET_KEY = SECRET_KEY or 'visor-local-dev-key-no-secret'  # noqa: F405
