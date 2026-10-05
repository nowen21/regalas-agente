# Pendiente: el freno repite el mismo aviso por cada archivo

| | |
|---|---|
| **De dónde sale** | [H-1 · El freno repitió su aviso unas 1700 veces en una sola acción](../../sesion-3.md), en el resumen de la sesión del 2026-10-04 |

## El problema

Una orden `npm install` en `proyectos/cimiento/` creó unos 1700 archivos en `node_modules/` antes de que la carpeta estuviera en `.gitignore`. El freno, que compara lo que cambió con el plan después de cada orden (`adaptadores/claude-code/hook_despues.py`), devolvió un bloque de cuatro líneas por archivo, con el mismo texto en todos. Todo eso entró al contexto del agente.

## Por qué importa

Ese aviso ocupó del orden de 380 000 tokens en un solo turno, y se vuelve a leer en cada llamada que sigue. Es el tipo de gasto que mide el pendiente 119. Un aviso que dijera una vez el motivo y la carpeta, con el número de archivos, daría la misma información.
