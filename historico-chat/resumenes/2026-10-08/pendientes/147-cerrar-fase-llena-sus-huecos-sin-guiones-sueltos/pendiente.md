# Pendiente: cerrar una fase llena sus huecos sin guiones sueltos

| | |
|---|---|
| **De dónde sale** | H-2 de la [sesión del 2026-10-08](../../guiones-que-pasan-a-cimiento.md) |

## El problema

`manage.py cerrar_fase` (`proyectos/cimiento/core/herramientas/fase.py`) escribe los documentos de cierre y deja `«…»` en lo que un programa no puede saber: el resumen, los hallazgos, el veredicto. Cimiento no tiene cómo llenar esos huecos. El 2026-10-06 se llenaron con un guion suelto, [`llenar_marcas.py`](../../../../scripts/2026-10-06/llenar_marcas.py), y 25 archivos `.txt` con un valor por línea (`marcas_*_cierre.txt`, `marcas_*_estado.txt`, `marcas_*_resultado.txt`).

## Por qué importa

Cada fase que se cierra vuelve a necesitar el guion y sus archivos sueltos. El guion ya funciona y comprueba que el número de valores coincida con el de huecos, pero vive fuera de Cimiento y cada sesión tiene que encontrarlo. Se relaciona con el [pendiente 142](../142-los-documentos-de-cimiento-viven-en-la-base/pendiente.md): cada operación termina en un guion nuevo.
