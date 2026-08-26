# Funcionalidad implementada — Fase A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas (módulo Instalación)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** La estructura queda completa, instalar dos veces da lo mismo, el texto propio sobrevive, y funciona con rutas con espacios y tildes.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-003: CA-01, CA-02 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase probó lo que más daño podía hacer.** La estructura se crea desde hace versiones y ya tenía dieciséis casos. Lo que faltaba era la **idempotencia** —que instalar dos veces no cambie nada— y la **compatibilidad de rutas**, que hasta hoy se daba por buena leyendo el código.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Crear las carpetas con su índice | programa | [`instalar.py`](../../../../../validadores/instalar.py) · `instalar_estructura` | ✅ Ya existía | CP-001 |
| No pisar lo que ya está | programa | El mismo, en cada paso | ✅ Ya existía | CP-002 |
| Que dos pasadas den lo mismo | programa | El mismo | ✅ Ya existía | CP-003 |
| Que la revisión diga qué falta | programa | [`checklist.py`](../../../../../validadores/checklist.py) | ✅ Ya existía | CP-004 |
| Las cuatro exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `EstructuraDeCarpetas` | ✅ Escritas acá | 3 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | 13 archivos y sus carpetas, con índices | ✅ |
| CA-02 | El texto propio sobrevive; dos pasadas dan lo mismo | ✅ |
| Transversal · Límites | Un proyecto completo no cambia en nada | ✅ |
| Transversal · Compatibilidad | Espacios **y** tildes juntos, en Windows | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---:|
| Archivos que deja la instalación en un proyecto vacío | **13** |
| Archivos que cambian al instalar por segunda vez | **1** — el registro de versión, por su fecha |
| Archivos con texto propio que se perdieron | **0** |
| Instalación en ruta con espacios y tildes | **Funciona** |

**La excepción del registro de versión está bien y se dejó explícita:** ese archivo existe para decir *cuándo* se actualizó, así que cambiar de fecha es su trabajo. Compararlo como si tuviera que ser idéntico habría obligado a elegir entre una prueba en rojo permanente y una comparación laxa que no vigila nada.

---

## 4. Lo que se dejó dicho de esta casa

**El estándar no se instala a sí mismo.** `instalar.py` excluye su propio repositorio a propósito, y hay una prueba que lo comprueba. Por eso la revisión de instalación **no aplica acá**: lo que en un proyecto heredero es «falta el `CLAUDE.md` generado», en esta casa es «el `CLAUDE.md` lo escribe una persona y dice otra cosa».

Sin eso escrito, cualquiera que corra `validar.py checklist` en este repositorio lee un incumplimiento donde no lo hay.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| La idempotencia se prueba comparando **el contenido** de cada archivo, no solo la lista: crear los mismos nombres con contenido distinto también sería pisar | CP-003 del [resultado](resultado_pruebas.md) |
| La compatibilidad se prueba con espacios **y** tildes juntos, en la máquina real, no leyendo el código | Verificación 3 |
| El registro de versión se excluye de la comparación **con su motivo escrito**, no en silencio | La prueba `test_instalar_dos_veces_deja_el_mismo_resultado` |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Mostrar antes de hacer | [HU-002](../../HU-002-mostrar-antes-de-hacer/HU-002-mostrar-antes-de-hacer.md) |
| No pisar lo escrito, en la puesta al día | [HU-005](../../HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) |
| Poner al día lo ya instalado | [HU-006](../../HU-006-poner-al-dia/HU-006-poner-al-dia.md), ya cerrada |

**Lo que deja esta fase:** de lo que se probó, lo único que podía romper de verdad era reinstalar sobre un proyecto vivo. No rompe — y ahora hay una prueba que lo dice cada vez.
