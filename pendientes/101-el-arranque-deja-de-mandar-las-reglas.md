# Pendiente · El arranque deja de mandar las reglas

**Estado:** **hecho** el 2026-09-28, en la misma sesión que lo anotó. Lo construyó la fase `C` de HU-009 de EP-005 (39.4.0): el arranque dice cómo llegan las reglas en vez de mandarlas, y todo lo que entrega cabe en 10.000 caracteres. Los textos de la plataforma los corrigió la fase `A` de HU-005 de EP-016.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-009](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md), CA-04, fase `C`. Es la historia que decidió qué manda el arranque |
| **De dónde sale** | [H-1 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

Al abrir la sesión, el enganche de arranque (`adaptadores/claude-code/hook_sesion.py`) le entrega al agente tres cosas, medidas el 2026-09-28:

| Parte | Quién la arma | Tamaño |
|---|---|---|
| Las reglas de `00` y `01` enteras, y el índice del resto | `validadores/cargador.py` | 89,7 KB |
| El índice de los recuerdos | `validadores/recuerdos.py` | 8,1 KB |
| El índice de las últimas conversaciones | `validadores/historico.py` | 5,2 KB |

La herramienta guarda aparte lo que un enganche entregue por encima de **10.000 caracteres**, y al agente le deja ver solo un avance de 2.000, sin pedirle que lea el resto (documentación oficial de Claude Code, `hooks.md`, sección «JSON output»; el límite es por enganche y no se puede subir). El archivo aparte queda fuera del repositorio, en el almacén de la herramienta. Sin las reglas, las otras dos partes suman 13,3 KB y también pasan el tope.

**La causa está escrita en el propio enganche.** `hook_sesion.py` fija `TOPE_DEL_CANAL` en 72 KB, a partir de una medición del 2026-09-15 que creyó que el corte estaba cerca de 80 KB. El límite real es siete veces menor.

Desde la versión 39.3.0 las reglas ya le llegan al agente con cada mensaje, por el recuperador y el mapa de tareas (HU-023 de EP-005). Mandarlas también al arrancar no aporta nada: la herramienta las corta.

El `CLAUDE.md` de este repositorio y [plantillas/CLAUDE.md.plantilla](../plantillas/CLAUDE.md.plantilla) todavía dicen que al arrancar se cargan todos los archivos numerados de `base/`.

## Por qué importa

- Lo que la herramienta guarda aparte queda fuera del repositorio, y eso incumple [`01·C29`](../base/01-conducta.md#c29--guarda-dentro-del-repositorio-todo-lo-del-agente-y-del-proyecto).
- El agente recibe un comienzo cortado y sin aviso, y puede creer que tiene las reglas cuando no las tiene. Fue lo que abrió la sesión del 2026-09-28.
- El índice de los recuerdos también llega cortado, y con él las preferencias del usuario.

## Qué falta

1. **El arranque deja de mandar las reglas.** En su lugar, una instrucción corta: las reglas llegan con cada mensaje, y ante una tarea se leen las que el mapa `base/mapa-de-tareas.md` pone bajo ella.
2. **Todo lo que manda el arranque cabe en 10.000 caracteres**, y `TOPE_DEL_CANAL` pasa a medir eso. El índice de recuerdos y el de conversaciones se recortan hasta caber, o se reemplazan por dónde encontrarlos.
3. **El `CLAUDE.md` del repositorio y su plantilla** dicen cómo llegan ahora las reglas, en vez de pedir cargarlas todas.
4. **Una prueba** que falle si lo que manda el arranque pasa de 10.000 caracteres.

## El límite

No cambia cómo el recuperador elige las reglas de cada mensaje, ni el recordatorio fijo de `hook_reglas.py`.

## Cómo se sabrá que cerró

- Lo que entrega `hook_sesion.py`, medido como lo lee la herramienta, tiene 10.000 caracteres o menos en este repositorio y en un proyecto instalado.
- Una prueba lo comprueba y falla si pasa del tope.
- El `CLAUDE.md` y su plantilla ya no piden cargar todos los archivos de `base/`.
- `python validadores/validar.py estandar` termina sin incumplimientos.
