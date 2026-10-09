# Pendiente: Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

| | |
|---|---|
| **De dónde sale** | [Hallazgo V2 de H-1 · Cimiento no sabe qué parte del programa de cada proyecto queda sin pruebas, ni lo exige](../../../2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md), según el [análisis 1](analisis-1.md), y [hallazgo V2 de H-2 · El plan de la EP-029·HU-001 no declara la migración que piden los ajustes nuevos](../../../2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md), según el [análisis 2](analisis-2.md), y [hallazgo V2 de H-3 · El plan de la EP-029·HU-002 no declara la sección del manual que pide toda pantalla nueva](../../../2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md), según el [análisis 3](analisis-3.md), en el resumen de la sesión del 2026-10-07 |

## El problema

Ningún proyecto mide qué parte de su programa queda sin pruebas; la configuración de cada proyecto no lo exige ni guarda el estado; ninguna prueba usa un navegador real; y cada proyecto tiene una copia de su configuración, `.agente/configuracion.md`, que ningún programa lee. Además, el plan de la HU-001 tiene que declarar la migración de `core/proyectos/`, y los planes que cambian la base tienen que listar antes todo lo que el marco va a pedir. El plan de la HU-002 tiene que declarar la sección del manual, y los planes que crean pantallas tienen que buscar antes qué piezas les exigen las pruebas.

## Por qué importa

Un hueco sin medir no se ve, una exigencia que no está en la configuración no se cumple, y una copia que nadie lee termina con datos viejos que alguien puede creer ciertos. Y una fase no debe detenerse por un archivo que se podía prever.
