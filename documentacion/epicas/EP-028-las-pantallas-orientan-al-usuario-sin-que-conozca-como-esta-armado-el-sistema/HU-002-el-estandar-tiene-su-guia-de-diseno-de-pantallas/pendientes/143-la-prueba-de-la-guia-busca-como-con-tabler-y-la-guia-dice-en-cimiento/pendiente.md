# Pendiente: la prueba de la guía de pantallas busca «Cómo con Tabler» y la guía ya dice «En Cimiento»

| | |
|---|---|
| **De dónde sale** | [H-4 · La prueba de la guía de pantallas está en rojo](../../../../../../historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md), en el resumen de la sesión del 2026-10-07 |

## El problema

`test_cp002_cada_seccion_de_construccion_dice_como_con_tabler` (`proyectos/cimiento/core/estandar/tests_guia.py`, línea 45) exige que las secciones 1 a 13 de `base/17-guia-de-pantallas.md` traigan «**Cómo con Tabler.**». La sección 13, «Documentación», trae «**En Cimiento.**», con AdminLTE 4.10.0. El cambio de plantilla de la EP-028·HU-007 no puso al día la prueba, o la guía.

## Por qué importa

La suite de `core.estandar` queda con una prueba en rojo que nadie vio, y la próxima fase que la corra la confunde con un defecto suyo.
