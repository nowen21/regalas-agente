# Pendiente: probar que las pruebas sirven con un solo comando

| | |
|---|---|
| **De dónde sale** | H-3 de la [sesión del 2026-10-08](../../guiones-que-pasan-a-cimiento.md) |

## El problema

Para saber si una prueba detecta un error, se daña el código a propósito y se mira si la prueba falla. Cimiento no tiene un comando para eso: en `historico-chat/scripts/` hay unos 20 guiones `sabotaje_*` y `sabotajes_*`, del 2026-08-25 en adelante, que repiten los mismos pasos: copiar el archivo, cambiar un texto, correr las pruebas, devolver el archivo desde la copia y borrar lo que el daño dejó escrito. Solo cambia la lista de daños.

## Por qué importa

Cada guion trae en su encabezado las lecciones de los anteriores: devolver desde la copia y no desde git, porque el código puede no estar guardado ([`sabotaje_c.py`](../../../../scripts/2026-08-25/sabotaje_c.py)); terminar corriendo todas las pruebas; borrar lo que el daño escribió fuera del archivo ([`sabotaje_e.py`](../../../../scripts/2026-08-25/sabotaje_e.py)). Si un guion nuevo olvida una, el código puede quedar dañado sin que nadie lo note. Se relaciona con el [pendiente 142](../142-los-documentos-de-cimiento-viven-en-la-base/pendiente.md).
