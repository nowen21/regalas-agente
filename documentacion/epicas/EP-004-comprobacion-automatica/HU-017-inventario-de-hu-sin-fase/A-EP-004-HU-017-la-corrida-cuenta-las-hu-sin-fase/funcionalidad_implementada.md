# Funcionalidad implementada — Fase A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase (módulo Comprobación automática)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** La corrida termina diciendo `HU: 68 en total · 25 completas · 43 incompletas`, y los tres números **coinciden con los que el pendiente 48 lleva a mano** — cruce que quedó como prueba permanente.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase` |
| **Módulo** | Comprobación automática — [`validadores/fases.py`](../../../../../validadores/fases.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-017: CA-01 a CA-04 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Versión** 23.3.0 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Esta sí construye.** De las doce fases ejecutadas hoy es la primera que escribe programa y no solo pruebas: la línea del inventario no existía.

Antes, saber cuántas HU tenían su fase completa era abrir el [pendiente 48](../../../../../pendientes/48-inventario-hu.md) y confiar en que alguien lo hubiera puesto al día. Ahora sale de recorrer el árbol, y las dos cuentas se comparan solas.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Contar total, completas e incompletas | programa | [`fases.py`](../../../../../validadores/fases.py) · `inventario()` | ✅ **Construido acá** | CP-001 |
| La línea al final de la corrida | programa | `fases.py` · `linea_inventario()` y [`validar.py`](../../../../../validadores/validar.py) · `cmd_fases` | ✅ **Construido acá** | CP-001 |
| Completa solo si **todas** sus fases lo están | programa | `inventario()` · el `all()` sobre las fases | ✅ **Construido acá** | CP-003 |
| Los tres bordes | programa | `inventario()` | ✅ **Construido acá** | CP-004 |
| Qué cuenta y qué se considera completa | documentación | [`docs/fases.md`](../../../../../validadores/docs/fases.md) | ✅ Escrito acá | — |
| Las seis exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `InventarioDeHU` | ✅ Escritas acá | 11 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | La corrida termina con los tres números, por el camino real | ✅ |
| CA-02 | 68 contadas a mano = 68 del programa, y los tres coinciden con el pendiente 48 | ✅ |
| CA-03 | Con una de las dos fases a medias, la HU cuenta incompleta | ✅ |
| CA-04 | Épica sin HU y carpeta `HU-` sin su `.md`: los dos definidos | ✅ |
| Transversal · Límites | Árbol vacío, épica sin HU y HU sin archivo: ninguno revienta | ✅ |
| Transversal · No regresión | Los 43 avisos siguen saliendo uno por uno | ✅ |

---

## 3. Las tres decisiones que tomó, y por qué

| Decisión | La alternativa | Por qué esta |
|---|---|---|
| Completa **solo si todas** sus fases lo están | Con que una lo esté | Con dos fases y una a medias la historia no está terminada. Contarla completa escondería justo el trabajo que falta — y hacerlo visible es lo único que este inventario hace |
| La carpeta `HU-` **sin su archivo** cuenta, como incompleta | No contarla | Existe **como trabajo** aunque le falte el papel. No contarla la volvería invisible, que es lo contrario de lo que se busca |
| Sin `documentacion/epicas/` **calla**, no falla | Reportar la falta | Quien la reporta ya es `validar()`. Dos hallazgos por lo mismo es ruido, y el ruido es lo que hace que se deje de leer |

**Y la de dónde va la línea:** al final, después de los hallazgos, **aunque no haya ninguno**. Es el resumen de cuánto falta, no un incumplimiento — y cuando no hay hallazgos es cuando más se quiere leer.

---

## 4. El cruce, que es lo que más vale

| | Programa | Pendiente 48, a mano |
|---|---:|---:|
| Total | 68 | 68 |
| Completas | 25 | 25 |
| Incompletas | 43 | 43 |

**Los tres coinciden, y quedó una prueba que los compara en cada corrida.** Con eso, el inventario escrito deja de ser «una tabla que alguien mantiene» y pasa a ser una tabla **verificada**: el día que se separen, la suite lo dice antes que nadie.

Es lo que el pendiente 48 pedía desde su primera línea — *«La HU-017 es la que hace esta cuenta sola»*.

---

## 5. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el pendiente 48 se **actualice** solo, y no solo se compare | Sin destino. Hoy se compara, que era lo que la HU pedía |
| El número de pendiente libre | [HU-018](../../HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md) |
| La corrida completa en una línea | [HU-008](../../HU-008-corrida-completa/HU-008-corrida-completa.md) |

**Lo que deja esta fase:** hasta hoy, «cuántas HU tienen su fase» se respondía abriendo un archivo y confiando en quien lo escribió. Ahora se responde corriendo el validador, y las dos respuestas tienen que dar lo mismo.
