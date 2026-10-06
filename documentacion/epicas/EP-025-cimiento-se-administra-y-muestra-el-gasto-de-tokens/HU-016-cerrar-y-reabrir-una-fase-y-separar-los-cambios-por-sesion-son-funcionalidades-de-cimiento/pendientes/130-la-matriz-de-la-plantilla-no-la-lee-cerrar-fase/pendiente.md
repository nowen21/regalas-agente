# Pendiente: la plantilla del plan de pruebas y `cerrar_fase` piden la matriz de dos formas distintas

| | |
|---|---|
| **De dónde sale** | [H-4 · La plantilla del plan de pruebas y `cerrar_fase` piden la matriz de dos formas distintas](../../../../../../historico-chat/resumenes/2026-10-05/sesion-2.md), en el resumen de la sesión del 2026-10-05 |

## El problema

La plantilla del plan de pruebas pide, en su matriz de trazabilidad, cada `CA-0N` y cada `CP-00N` como enlace, y deja poner varios casos en una fila. `Fase.casos()`, en [fase.py](../../../../../../proyectos/cimiento/core/herramientas/fase.py), solo lee filas con un caso cada una y los nombres sin enlace; si no encuentra ninguna, `manage.py cerrar_fase` dice «no tiene casos en su matriz» y no cierra. También toma como «en plantilla» un plan cuyo título conserva las comillas «» de la plantilla, aunque esté lleno. Se vio el 2026-10-06 al cerrar `B-EP-025-HU-025-retapar-lo-guardado`.

## Por qué importa

Quien sigue la plantilla al pie de la letra escribe una matriz que la herramienta de cierre no lee, y el cierre falla sin decir que el problema es el formato; para cerrar hay que desobedecer la plantilla.
