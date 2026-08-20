# Pendiente · La suite de `validadores/tests/` tiene dos fallas que no son de ninguna fase abierta

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-008 — Corrida completa](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) — es la corrida entera la que está en rojo por causas ajenas al trabajo del día |
| **De dónde sale** | El H-4 del resumen [../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md): la no regresión de las tres fases del día (CP-008) |
| **Proyecto de origen** | El estándar mismo |

## El problema

Al correr `validadores/tests/` entera para cerrar las fases del 2026-08-20, dos pruebas fallan por cosas que ninguna de esas fases tocó:

1. **`test_ningun_resumen_del_repositorio_queda_ilegible`**: [../historico-chat/resumenes/2026-08-19/sesion-3.md](../../historico-chat/resumenes/2026-08-19/sesion-3.md) tiene un hallazgo escrito `### 1 ·` sin la `H-` del molde. Es del día anterior; el programa lo cuenta como resumen vacío.
2. **`test_cero_entre_carpetas_fuera_de_prompts`** (`13·DOC14`): cuatro enlaces cuyo texto no dice dónde vive el archivo, en `evals/README.md` (1), `historico-chat/README.md` (1) y `historico-chat/resumenes/README.md` (2). Los dos últimos archivos los escriben **los enganches** (`historico.py` e `_indexar_dias` de `resumen.py`): el texto del enlace que generan es `2026-08-20/`, no la ruta desde la raíz.

## Por qué importa

Una suite en rojo por causas viejas esconde la falla nueva: hoy hubo que leer las siete fallas una por una para separar las tres de la sesión de las previas. Y el punto 2 es un programa escribiendo enlaces que el propio estándar reprueba: cada sesión nueva agrega uno.

## Qué falta

- Renumerar el hallazgo de `sesion-3.md` (una línea).
- Que `historico.py` y `resumen.py` escriban el texto del enlace con la ruta desde la raíz, como pide `DOC14`, y corregir los cuatro que ya están.

## El límite

No toca qué dicen los resúmenes ni los índices; solo la forma del encabezado y del enlace.

## Cómo se sabrá que cerró

`python -m unittest discover -s validadores/tests -p "test_*.py"` termina en `OK`, y abrir una sesión nueva no vuelve a dejar un enlace que `DOC14` reprueba.
