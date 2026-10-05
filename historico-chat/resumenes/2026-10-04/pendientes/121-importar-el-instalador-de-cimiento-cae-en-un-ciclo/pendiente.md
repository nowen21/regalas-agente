# Pendiente: importar el instalador de Cimiento cae en un ciclo

| | |
|---|---|
| **De dónde sale** | [H-3 · Las pruebas del instalador de Cimiento no cargan solas](../../sesion-3.md), en el resumen de la sesión del 2026-10-04 |

## El problema

`proyectos/cimiento/core/validadores/__init__.py` tiene, sin guardar, una línea nueva que importa `checklist`. Con ella se forma un ciclo: `core.herramientas.instalar` importa `core.validadores.version`, eso carga `core/validadores/__init__.py`, que importa `checklist`, que importa `core.enganches.sesion`, y `sesion` vuelve a importar `core.herramientas.instalar` a medio cargar. Ese cambio lo dejó otra sesión.

Lo que se rompe hoy:

- `python manage.py test core.herramientas.tests_instalacion` falla al importar, antes de correr una sola prueba.
- `python -c "from core.herramientas.instalar import Instalador"` falla; `python -m core.herramientas.instalar` también.

Funciona solo si antes se importa `core.validadores`. `validadores/instalar.py` lo hace así desde `EP-025·HU-001`.

## Por qué importa

Las pruebas del instalador no corren, así que un cambio al instalador no tiene red. Y quien importe el instalador en otro orden se encuentra un error que no dice dónde está el ciclo.
