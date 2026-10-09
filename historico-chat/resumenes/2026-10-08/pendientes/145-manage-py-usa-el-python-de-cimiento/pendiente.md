# Pendiente: `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes

| | |
|---|---|
| **De dónde sale** | [H-4 · La consulta de las reglas falla porque el aviso manda a usar el Python que no tiene el conector de MySQL](../../los-documentos-de-cimiento-pasan-a-su-base.md), según el [análisis 1](analisis-1.md), y [H-5 · El freno detuvo una edición fuera del plan](../../los-documentos-de-cimiento-pasan-a-su-base.md), según el [análisis 2](analisis-2.md), en el resumen de la sesión del 2026-10-08 |

## El problema

El aviso de cada sesión manda a leer las reglas con `python "…/proyectos/cimiento/manage.py" ver_estandar <ruta>` (`proyectos/cimiento/core/enganches/cargador.py:68`; también `proyectos/cimiento/core/herramientas/recuperar.py:319`). Ese `python` es el del computador, que no tiene el conector de MySQL, y la consulta termina con `ModuleNotFoundError: No module named 'MySQLdb'`. Cimiento usa su propio Python 3.11.9, en `proyectos/cimiento/.venv/`, y con ese la misma consulta funciona.

Con el Python de Cimiento, las tildes salen dañadas en la consola de Windows.

El usuario aprobó la solución el 2026-10-08: que `manage.py` revise con qué Python lo abrieron y, si no es el de Cimiento, se vuelva a abrir solo con ese; y que escriba la salida de forma que las tildes salgan bien. Va con una prueba que lo abre con el Python del computador y confirma que la consulta funciona.

## Por qué importa

Toda sesión, en cualquier proyecto, recibe la orden de leer las reglas con un comando que falla; sin leerlas, trabaja sin las reglas completas.
