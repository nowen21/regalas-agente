# Plan de Trabajo — Fase A-EP-005-HU-011-donde-termina-el-estandar   ·   `[CAPA 3]`

**Para qué sirve.** Dice **qué se va a hacer y sobre qué archivos**, antes de tocar nada. No se ejecuta hasta el OK del usuario ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-011-donde-termina-el-estandar` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-011](../HU-011-donde-termina-el-estandar.md) |
| **CA que cubre** | `CA-01`, `CA-02`, `CA-03` |
| **Fecha** | 2026-08-18 |

**ORIGEN**: 🔀 **híbrido**. `CA-01` y `CA-02` se **retro-documentan** — el mapa se escribió el 2026-08-18 al bajar el punto 1 del [pendiente 15](../../../../../pendientes/hecho/el-estandar-depende-de-una-sola-herramienta.md). `CA-03` es ✨ **funcionalidad nueva**: no existe.

## 1. Objetivo

**Que el mapa no envejezca en silencio.** Hoy [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md) dice cuáles de las 53 piezas están amarradas. **Un archivo nuevo bajo `validadores/` no aparece ahí hasta que alguien se acuerde** — y eso es lo que le pasa a todo mapa escrito a mano.

**Entra:** la comprobación de que ninguna pieza quede sin clasificar, y la retro-documentación de lo ya escrito.

**No entra:** mover el adaptador a una carpeta propia (punto 2 del pendiente) ni escribir el contrato de qué necesita el estándar de cualquier agente (punto 3). **Ninguno de los dos lo cubre un criterio de esta historia.**

## 2. Línea base verificada — 2026-08-18

| Qué | Cuánto |
|---|---|
| Piezas en `validadores/` | **53** |
| Amarradas a la herramienta | 18 |
| Libres | 35 |
| Nombradas en el mapa hoy | las 18 amarradas, una por una; las libres **por su total, no por su nombre** |

**Ese es el hueco que `CA-03` destapa:** el mapa nombra lo amarrado y **cuenta** lo libre. Una pieza nueva que no toque la herramienta entra en el total sin que nadie la haya mirado — y si sí la toca, no aparece en ningún lado.

## 3. Tareas

| # | Tarea | CA | Archivo |
|---|---|---|---|
| T-01 | `amarre.py`: medir las marcas de herramienta por pieza, con la misma lista con que se hizo el mapa | CA-01 | `validadores/amarre.py` (nuevo) |
| T-02 | Reportar **la pieza que el mapa no nombra** y trae marcas | CA-03 | el mismo |
| T-03 | Reportar **la pieza que el mapa nombra y ya no existe** — el mapa envejece por los dos lados | CA-03 | el mismo |
| T-04 | Subcomando `validar.py amarre` con el recuento al final | CA-01 | `validadores/validar.py` |
| T-05 | Que el mapa liste **las 35 libres por su nombre**, no por su total | CA-01, CA-02 | el mapa |
| T-06 | Casos automatizados | todos | `validadores/tests/test_el_mapa_del_amarre_no_envejece.py` (nuevo) |
| T-07 | Retro-documentar `CA-01` y `CA-02` en el resultado, con la medición del 2026-08-18 | CA-01, CA-02 | `resultado_pruebas.md` |
| T-08 | Versionar y cerrar trazabilidad | — | `VERSION` · `CHANGELOG.md` · la HU |

## 5. Verificación

| CA | Cómo |
|---|---|
| CA-01 | Las 53 piezas tienen columna. El recuento del programa **coincide** con lo escrito en el mapa |
| CA-02 | Cada pieza amarrada dice qué se pierde si cambia el agente |
| CA-03 | Se agrega un archivo de prueba a `validadores/` y **se reporta**; se clasifica y deja de reportarse |

## 7. Reversión

Un programa nuevo y una sección del mapa. Se borran y se revierte el commit.

## 9. Reglas aplicadas

`20·M9` (declarar si es validable) · `20·M10` (versionar) · `02·F17` (línea base contra el repositorio) · `13·DOC12` (origen híbrido declarado).

## 10. Riesgos

| # | Riesgo | Qué se hace |
|---|---|---|
| R-01 | Que el programa y el mapa midan distinto y nadie lo note | El programa usa **la misma lista de marcas** con que se escribió el mapa, y un caso compara los dos recuentos |
| R-02 | Que el mapa con 53 nombres se vuelva ilegible | Las libres van en una lista compacta, no en tabla; lo que se lee de a una es lo amarrado |
| R-03 | Que el propio `amarre.py` cuente sus marcas y se reporte a sí mismo | Se exceptúa por nombre, como se hizo con los datos de prueba del detector de secretos |
